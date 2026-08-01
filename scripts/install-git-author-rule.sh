#!/usr/bin/env bash
# Install org-wide Cursor rule: Venkata Peetla is always git author/committer.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
RULE_SRC="$ROOT_DIR/rules/git-author-venkata.mdc"
USER_RULES_DIR="${HOME}/.cursor/rules"
SKILL_SRC="$ROOT_DIR/skills/git-commit-author"

if [[ ! -f "$RULE_SRC" ]]; then
  echo "Missing $RULE_SRC" >&2
  exit 1
fi

mkdir -p "$USER_RULES_DIR"
cp "$RULE_SRC" "$USER_RULES_DIR/git-author-venkata.mdc"
echo "User rule → $USER_RULES_DIR/git-author-venkata.mdc (alwaysApply — every repo)"

mkdir -p "${HOME}/.cursor/skills"
rm -rf "${HOME}/.cursor/skills/git-commit-author"
cp -R "$SKILL_SRC" "${HOME}/.cursor/skills/git-commit-author"
echo "Global skill → ${HOME}/.cursor/skills/git-commit-author"

echo "Done. This applies to the entire vpeetla-ai org and any other clone Cursor opens."
