# Week 11 — Concept fence

## Allowed

**Everything from weeks 1 to 10**, plus:

- sampling, temperature and top-k by hand
- `shoplab.llm`: `get_llm()`, `.complete(messages, system=...)`, `Reply`, `PRICES`
- pydantic `BaseModel`, `Literal`, `model_validate`; JSON
- regular expressions as a guardrail

## Not yet

tool use and agents (the `agent` course) · retrieval (the `RAG` course) · fine-tuning an LLM (the
`fine-tuning` course) · streaming · prompt caching · LangChain and other frameworks · calling a
provider's SDK directly from your lab files

---

## Why every lab goes through `shoplab.llm` and a fake

Tests that call a real model cost money, need a key, and give a different answer every
run, so they cannot be red or green. The fake is deterministic and fails on purpose — bad
JSON, missed negation, obedience to injected instructions — so your retry, comparison and
guardrail code can be tested against those failures. The price is honesty: every LLM
number your tests produce describes your code, not any real model. The runbook has the
live run that measures the real one.
