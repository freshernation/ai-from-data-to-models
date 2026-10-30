# Day 2 — A model behind an API

> **By the end of today** you can hold a conversation with a language model through a
> client, and say what each turn cost and why the tenth turn sends seventeen times as many tokens as the first.

---

## Read first

- [ ] Anthropic — [Messages API](https://docs.anthropic.com/en/api/messages) — the request body: `model`, `system`, `messages`, and the `usage` field of the response · 15 min
- [ ] Anthropic — [Pricing](https://www.anthropic.com/pricing) — the API table · 5 min
- [ ] `shoplab/llm.py` in this repo — the whole file · 10 min

---

## What you need to know

### One function

`get_llm().complete(messages, system=...)` returns a `Reply`: the text, the input and
output tokens, the latency and the model. Behind it is either the scripted fake (always,
in tests) or Claude. Your lab code never imports a provider's SDK, so swapping models is
one environment variable.

### Tokens are money

A provider charges per million tokens, input and output separately. `shoplab.llm.PRICES`
holds Anthropic's published rates (checked 2026-10-29): `claude-opus-5-5` $4 in / $20
out, `claude-haiku-5-5` $0.10 / $0.50. Prices change; check the page before you quote one.

### The model remembers nothing

To hold a conversation you send the whole history every time. Ten questions about an
order: turn 1 sends **25** tokens, turn 10 sends **424**. Ten turns cost **2,211** input
tokens with memory and **250** without. Cost grows with the square of the conversation.
(Token counts here come from the fake's estimate of four characters per token.)

---

## Exercises

```bash
pytest week-11/day-2 -v
```

Write `user`, `cost`, `Chat`, `tokens_sent` and `per_thousand` in `ask.py`.

---

## Predict-then-run

What will 1,000 ten-turn conversations cost on `claude-opus-5-5`, in dollars? Then on
`claude-haiku-5-5`? Work it out before running.

---

## Before you close the laptop

Commit, push, fill in the signal log.
