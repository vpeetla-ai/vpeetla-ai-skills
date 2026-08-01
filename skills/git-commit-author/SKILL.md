---
name: git-commit-author
description: >-
  ALWAYS set Venkata Peetla as git author and committer on EVERY commit and PR
  in ANY repository (entire vpeetla-ai org and any other clone). Use whenever
  committing, pushing, or running gh pr create — not limited to one repo.
---

# Git commit author — Venkata Peetla (org-wide)

## Scope

**All repos. All the time.** Every `github.com/vpeetla-ai/*` repo, every local clone,
new repos, playbooks, portfolio, spine, labs, stubs, handbook, skills — anything.

If you are about to run `git commit` or `gh pr create`, this skill applies.

## Required identity

| Field | Value |
|-------|--------|
| Name | `Venkata Peetla` |
| Email | `vpeetla.ai@gmail.com` |
| GitHub | `vpeetla-ai` |

Author **and** committer must both be Venkata.

## Commit command

Do **not** rewrite `git config`. Pass identity per commit:

```bash
export GIT_AUTHOR_NAME="Venkata Peetla"
export GIT_AUTHOR_EMAIL="vpeetla.ai@gmail.com"
export GIT_COMMITTER_NAME="Venkata Peetla"
export GIT_COMMITTER_EMAIL="vpeetla.ai@gmail.com"
git -c user.name="Venkata Peetla" -c user.email="vpeetla.ai@gmail.com" \
  commit --author="Venkata Peetla <vpeetla.ai@gmail.com>" \
  -m "$(cat <<'EOF'
Commit message.

EOF
)"
```

## Forbidden

- `Co-authored-by: Cursor` / `cursoragent@cursor.com`
- Author or committer of `Cursor`, `cursoragent`, or `GitHub <noreply@github.com>`
- Assuming the rule only applies to one workspace

## PRs

- `gh pr create` as authenticated `vpeetla-ai`
- No “Made with Cursor” footer unless Venkata asks

## Install (user-global)

```bash
./scripts/install-git-author-rule.sh
./scripts/install.sh --cursor --global
```
