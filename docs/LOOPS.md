# LOOPS — Field notes on agents that run for days

Org reference distilled from Andrej Karpathy's [autoresearch](https://github.com/karpathy/autoresearch) pattern and loop-engineering practice across [vpeetla-ai](https://github.com/vpeetla-ai).

## When to add a LOOPS.md in a repo

- Overnight or multi-hour agent runs
- Self-improving harnesses (LoopForge ODAEU, RAG tuning)
- Any loop where the agent edits code and an objective metric decides keep vs discard

## Quick template

Copy into `docs/LOOPS.md` in the target repo:

1. **Who this loop serves** — user role + job-to-be-done
2. **One metric** — single comparable number + direction
3. **Mutable surface** — what the agent may change (one file or bounded tools)
4. **Locked eval** — pytest, golden queries, gateway — agent cannot modify
5. **Time budget** — fixed wall clock per iteration
6. **Loop protocol** — hypothesize → act → measure → keep/discard
7. **Stop conditions** — iterations, cost, plateau
8. **Learnings log** — append-only memory across rounds

## Repo mappings

| Repo | LOOPS.md location | Mutable surface | Locked eval |
|------|-------------------|-----------------|-------------|
| loop-engine-agent-platform | `docs/LOOPS.md` | RAG config, repo patches | pytest, review score |
| enterprise_rag_platform | `docs/LOOPS.md` | retrieval params | `tests/fixtures/golden_queries.json` |
| ai-content-factory | optional | draft prompts (dev only) | HITL + gateway + pytest |
| vllm-architecture-lab | N/A (edu) | simulator params | `tests/test_engine.py` |

## Skill

Cursor/Codex: use skill **`agents-that-run-for-days`** for implementation guidance.

## Further reading

- Skill: `skills/agents-that-run-for-days/SKILL.md`
- Skill: `skills/loop-engineering/SKILL.md`
- Case study: [LoopForge](https://github.com/vpeetla-ai/ai-architecture-portfolio/blob/main/case-studies/loopforge-self-improving-harness.md)
