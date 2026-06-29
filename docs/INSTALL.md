# Installation Guide

Skills work in **Cursor** (`.cursor/skills/`) and **Codex / Claude Code** (`AGENTS.md` + `CONTEXT.md`).

## Prerequisites

```bash
git clone https://github.com/vpeetla-ai/vpeetla-ai-skills.git
cd vpeetla-ai-skills
chmod +x scripts/install.sh
```

## Cursor

### Global (all projects)

```bash
./scripts/install.sh --cursor --global
```

Skills install to `~/.cursor/skills/<skill-name>/SKILL.md`.

Cursor discovers them automatically when the task matches the skill `description` in frontmatter.

### Per project (recommended for org repos)

```bash
./scripts/install.sh --cursor --project /path/to/loop-engine-agent-platform
```

Skills install to `.cursor/skills/` inside that repo — commit them so teammates get the same agent behavior.

### Verify

1. Open the project in Cursor
2. Start a chat: "Which stack layer is ai-content-factory?"
3. Agent should load **governed-ai-stack** vocabulary from CONTEXT.md

## Codex / Claude Code

```bash
./scripts/install.sh --codex --project /path/to/venkat-ai-platform
```

Copies:

- `AGENTS.md` — root agent instructions (Karpathy + org conventions)
- `CONTEXT.md` — shared domain vocabulary

Existing files are backed up with a timestamp suffix.

### Verify

Open the repo in Codex; root instructions should reference the 6-layer stack and gateway rules.

## Both editors at once

```bash
./scripts/install.sh --cursor --codex --project /path/to/your-repo
```

## First-time repo bootstrap

After install, run the **setup-vpeetla-skills** skill (or ask the agent to follow it):

- Creates `.vpeetla-skills.json` with issue tracker and stack layer
- Confirms `docs/` path and honest README status table

## Updating skills

```bash
cd vpeetla-ai-skills
git pull
./scripts/install.sh --cursor --codex --project /path/to/repo
```

## Symlink alternative (advanced)

```bash
ln -sf ~/vpeetla-ai-skills/skills ~/.cursor/skills/vpeetla-ai
```

Not recommended for per-repo installs — use `install.sh` for reproducible copies.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Skills not loading in Cursor | Check `.cursor/skills/*/SKILL.md` exists; restart Cursor |
| Codex ignores CONTEXT | Ensure `AGENTS.md` at repo root references CONTEXT.md |
| Duplicate AGENTS.md | Restore from `AGENTS.md.bak.*` and merge manually |
