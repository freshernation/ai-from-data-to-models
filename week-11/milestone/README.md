# Week 11 Milestone — A reply drafter that cannot be talked into a refund

> Your sentiment model decides, the LLM drafts, a guardrail checks every draft, and
> `GUARDRAILS.md` says what was attacked, what got through, and what still could.

---

## The files

| File | Where it comes from |
|---|---|
| `text.py`, `trainer.py`, `embeddings.py`, `lstm.py`, `sentiment.py` | **copy** from week 9 (and week 7's `trainer.py`) |
| `drafter.py` | new: `RULES`, `guardrail`, `draft`, `audit` |
| `GUARDRAILS.md` | new |

## `GUARDRAILS.md`

| Section | What goes in it |
|---|---|
| Who decides what | Your model, the LLM, the guardrail — each one's job |
| The attacks, and what happened | The audit's numbers, on attacks and on ordinary reviews |
| What the guardrail cannot catch | At least two attacks that would get through |
| Before this goes live | What you would run, and who stays in the loop |

At least 50 words each. Then paste it into `ai/editor.md` in red-team mode.

---

## Check it

```bash
pytest week-11/milestone -v
python week-11/milestone/drafter.py
```

## Friday

The instructor writes a new attack; you run it live.
