# vpeetla-ai Skills

### Agent skills for real engineering — Cursor, Codex, and Claude Code

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Org](https://img.shields.io/badge/GitHub-vpeetla--ai-blue)](https://github.com/vpeetla-ai)
[![Portfolio](https://img.shields.io/badge/🌐_venkat--ai.com-Portfolio-5eead4)](https://venkat-ai.com/work)

> Shared skills for the [vpeetla-ai](https://github.com/vpeetla-ai) reference stack — orchestration, governance, RAG, AgentOps, content, and loop engineering.
>
> Inspired by [mattpocock/skills](https://github.com/mattpocock/skills) (composable, small, test-driven) and [Andrej Karpathy's agentic engineering](https://www.youtube.com/watch?v=96jN2OCOfLs) (harness, eval loops, quality bar — not vibe coding).

---

## Quickstart (60 seconds)

### Cursor

```bash
git clone https://github.com/vpeetla-ai/vpeetla-ai-skills.git
cd vpeetla-ai-skills
./scripts/install.sh --cursor --global
```

Then in any project: mention a skill or run **`/setup-vpeetla-skills`** (if you symlink user skills).

Per-repo install:

```bash
./scripts/install.sh --cursor --project /path/to/loop-engine-agent-platform
```

Skills land in `.cursor/skills/` (project) or `~/.cursor/skills/` (global).

### Codex / Claude Code

```bash
./scripts/install.sh --codex --project /path/to/your-repo
```

Writes `AGENTS.md` + `CONTEXT.md` into the target repo (backs up existing files).

Or copy manually:

```bash
cp AGENTS.md CONTEXT.md ../your-repo/
```

---

## Skill catalog

| Skill | Invoke | Purpose |
|-------|--------|---------|
| [setup-vpeetla-skills](skills/setup-vpeetla-skills/) | User | One-time repo bootstrap (tracker, labels, docs path) |
| [grill-with-context](skills/grill-with-context/) | User | Align on plan + sharpen CONTEXT.md before big changes |
| [agentic-engineering](skills/agentic-engineering/) | Model | Karpathy discipline: think, simplify, surgical diffs, verify |
| [governed-ai-stack](skills/governed-ai-stack/) | Model | 6-layer map — which repo answers which question |
| [langgraph-orchestration](skills/langgraph-orchestration/) | Model | StateGraph nodes, routing, checkpointers, HITL interrupt |
| [aegis-gateway](skills/aegis-gateway/) | Model | Gateway before notify/publish/deploy side effects |
| [loop-engineering](skills/loop-engineering/) | Model | ODAEU harness, evolve RAG, procedural memory |
| [repo-fix-pr](skills/repo-fix-pr/) | User | LoopForge: clone → test → patch → branch → GitHub PR |
| [rag-governance](skills/rag-governance/) | Model | Access-before-ranking, hybrid retrieval, citations |
| [hitl-side-effects](skills/hitl-side-effects/) | Model | When to gate publish, deploy, notify, git push |
| [deploy-vercel-render](skills/deploy-vercel-render/) | Model | UI on Vercel, API on Render, `plan: free` |
| [tdd-agent-loops](skills/tdd-agent-loops/) | Model | Red-green-refactor for agent graph changes |
| [portfolio-adr](skills/portfolio-adr/) | User | ADRs, case studies, honest status tables |
| [mcp-tool-exposure](skills/mcp-tool-exposure/) | Model | MCP servers, tool bridge, 2026 tool-access layer |
| [production-observability](skills/production-observability/) | Model | Langfuse, OTel, trace + eval regression |
| [honest-status-table](skills/honest-status-table/) | User | README ✅/🟡/❌ tables; portfolio sync |
| [vllm-inference](skills/vllm-inference/) | Model | PagedAttention, batching, KV budget, GPU sizing |
| [agent-protocol-stack-2026](skills/agent-protocol-stack-2026/) | Model | Skills → MCP → Gateway → Observability |
| [enterprise-ai-architect](skills/enterprise-ai-architect/) | Model | Principal architect reviews, ADRs, honest trade-offs |

**User-invoked** — you type the skill name. **Model-invoked** — agent loads when task matches description.

---

## Shared vocabulary

Read [CONTEXT.md](CONTEXT.md) before working in any org repo. It defines terms like **harness**, **gateway**, **ODAEU**, **access-before-ranking**, and **loopforge/fix branch**.

---

## Which skill for which repo?

| Repo | Primary skills |
|------|----------------|
| venkat-ai-platform | governed-ai-stack, langgraph-orchestration, aegis-gateway |
| aegisai-enterprise-agent-platform | aegis-gateway, hitl-side-effects, portfolio-adr |
| enterprise_rag_platform | rag-governance, hitl-side-effects |
| aegisloop-agentops-workbench | governed-ai-stack, langgraph-orchestration, deploy-vercel-render |
| ai-content-factory | aegis-gateway, hitl-side-effects, langgraph-orchestration |
| loop-engine-agent-platform | loop-engineering, repo-fix-pr, tdd-agent-loops |
| vllm-architecture-lab | vllm-inference, agent-protocol-stack-2026 |
| vpeetla-ai-skills | agent-protocol-stack-2026, honest-status-table |
| agent-pattern repos | tdd-agent-loops, agentic-engineering |
| ai-architecture-portfolio | portfolio-adr, governed-ai-stack |

---

## Design principles (from matt + Karpathy)

1. **Small composable skills** — not a 200-page mega-prompt
2. **Feedback loops** — tests, eval gates, traces before ship
3. **Shared language** — CONTEXT.md reduces token waste
4. **Orchestration ≠ governance** — never mix VAP and AegisAI concerns
5. **Stub-first** — pattern repos run without API keys
6. **Honest READMEs** — implementation status tables, not marketing fiction

---

## Connect

- [venkat-ai.com/work](https://venkat-ai.com/work)
- [ai-architecture-portfolio](https://github.com/vpeetla-ai/ai-architecture-portfolio)
- [LoopForge live demo](https://demo-omega-taupe.vercel.app)

MIT License — fork and adapt for your org.
