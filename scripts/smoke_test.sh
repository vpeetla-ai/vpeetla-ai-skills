#!/usr/bin/env bash
# Smoke test: install skills into a temp project and verify files exist.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$TMP/project"
"$ROOT_DIR/scripts/install.sh" --cursor --codex --project "$TMP/project"

test -d "$TMP/project/.cursor/skills"
test -f "$TMP/project/AGENTS.md"
test -f "$TMP/project/CONTEXT.md"

SKILL_COUNT="$(find "$ROOT_DIR/skills" -name SKILL.md | wc -l | tr -d ' ')"
INSTALLED_COUNT="$(find "$TMP/project/.cursor/skills" -name SKILL.md | wc -l | tr -d ' ')"

if [[ "$SKILL_COUNT" != "$INSTALLED_COUNT" ]]; then
  echo "Expected $SKILL_COUNT skills, installed $INSTALLED_COUNT" >&2
  exit 1
fi

echo "smoke ok: $INSTALLED_COUNT skills installed"
