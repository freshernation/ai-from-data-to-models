# Day 3 — JSON you can trust

> **By the end of today** you can ask a model for JSON, check it against a schema, and
> retry with the error when it is wrong — and say what that costs.

---

## Read first

- [ ] Pydantic — [Models](https://docs.pydantic.dev/latest/concepts/models/) — "Basic model usage" and "Validating data" · 15 min
- [ ] Anthropic — [Structured outputs](https://docs.anthropic.com/en/docs/build-with-claude/structured-outputs) — the introduction · 5 min

---

## What you need to know

### A model's text is untrusted input

Ask for `{"label": "positive", "reason": "..."}` and you will sometimes get "Sure! Here
is my answer: {...}", or a label of "Positive!". Code that does `json.loads(reply)["label"]`
crashes on the first and quietly mislabels on the second.

### Validate, then retry with the error

A pydantic model with `label: Literal["positive", "negative"]` rejects both. When it
fails, send the bad answer back as the assistant's turn, say what was wrong, and ask again.

### The finding

On the 1,000 test reviews the fake gives **192** unusable first answers. One retry
rescues **all** of them — for **1,192** calls instead of 1,000: 19% more cost. Real APIs
can also constrain the output to your schema (structured outputs); you still validate,
because the content can be wrong even when the format is right.

---

## Exercises

```bash
pytest week-11/day-3 -v
```

Write `parse`, `classify` and `survey` in `structured.py`.

---

## Predict-then-run

With two retries instead of one, how many calls will 1,000 reviews take? Why?

---

## Before you close the laptop

Commit, push, fill in the signal log.
