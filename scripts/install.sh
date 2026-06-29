#!/usr/bin/env bash
# Install vpeetla-ai skills into Cursor or Codex/Claude Code projects.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_SRC="$ROOT_DIR/skills"

usage() {
  cat <<'EOF'
Usage: ./scripts/install.sh [OPTIONS]

Options:
  --cursor          Install Cursor Agent Skills (SKILL.md directories)
  --codex           Install Codex/Claude Code root files (AGENTS.md, CONTEXT.md)
  --global          Cursor: install to ~/.cursor/skills/ (default for --cursor)
  --project PATH    Target repo path (required for --project mode)

Examples:
  ./scripts/install.sh --cursor --global
  ./scripts/install.sh --cursor --project ../loop-engine-agent-platform
  ./scripts/install.sh --codex --project ../venkat-ai-platform
  ./scripts/install.sh --cursor --codex --project .

Both editors:
  ./scripts/install.sh --cursor --codex --project /path/to/repo
EOF
}

INSTALL_CURSOR=false
INSTALL_CODEX=false
GLOBAL=false
PROJECT=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --cursor) INSTALL_CURSOR=true; shift ;;
    --codex) INSTALL_CODEX=true; shift ;;
    --global) GLOBAL=true; shift ;;
    --project)
      PROJECT="${2:-}"
      if [[ -z "$PROJECT" ]]; then echo "Error: --project requires a path" >&2; exit 1; fi
      shift 2
      ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 1 ;;
  esac
done

if [[ "$INSTALL_CURSOR" == false && "$INSTALL_CODEX" == false ]]; then
  echo "Error: specify --cursor and/or --codex" >&2
  usage
  exit 1
fi

if [[ "$INSTALL_CURSOR" == true && "$GLOBAL" == false && -z "$PROJECT" ]]; then
  echo "Error: --cursor without --global requires --project PATH" >&2
  usage
  exit 1
fi

backup_if_exists() {
  local file="$1"
  if [[ -f "$file" ]]; then
    cp "$file" "${file}.bak.$(date +%Y%m%d%H%M%S)"
    echo "  backed up $(basename "$file")"
  fi
}

install_cursor_skills() {
  local dest="$1"
  mkdir -p "$dest"
  local count=0
  for skill_dir in "$SKILLS_SRC"/*/; do
    [[ -d "$skill_dir" ]] || continue
    local name
    name="$(basename "$skill_dir")"
    if [[ -f "$skill_dir/SKILL.md" ]]; then
      rm -rf "$dest/$name"
      cp -R "$skill_dir" "$dest/$name"
      count=$((count + 1))
    fi
  done
  echo "Cursor: installed $count skills → $dest"
}

install_codex_files() {
  local dest="$1"
  mkdir -p "$dest"
  backup_if_exists "$dest/AGENTS.md"
  backup_if_exists "$dest/CONTEXT.md"
  cp "$ROOT_DIR/AGENTS.md" "$dest/AGENTS.md"
  cp "$ROOT_DIR/CONTEXT.md" "$dest/CONTEXT.md"
  echo "Codex: wrote AGENTS.md + CONTEXT.md → $dest"
}

if [[ "$INSTALL_CURSOR" == true ]]; then
  if [[ "$GLOBAL" == true ]]; then
    install_cursor_skills "${HOME}/.cursor/skills"
  else
    PROJECT="$(cd "$PROJECT" && pwd)"
    install_cursor_skills "$PROJECT/.cursor/skills"
  fi
fi

if [[ "$INSTALL_CODEX" == true ]]; then
  if [[ -z "$PROJECT" ]]; then
    echo "Error: --codex requires --project PATH" >&2
    exit 1
  fi
  PROJECT="$(cd "$PROJECT" && pwd)"
  install_codex_files "$PROJECT"
fi

echo "Done. See docs/INSTALL.md for verification steps."
