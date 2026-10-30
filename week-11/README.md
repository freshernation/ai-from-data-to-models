# Week 11 — Generative AI

> **Destination**
> You can generate text by sampling and explain what temperature and top-k do, call a
> large language model through a tested client and say what each call costs, get JSON
> back that your code has checked, compare an LLM with your own model on accuracy, cost
> and speed, and ship a reply drafter whose guardrail stops a model that obeys an attacker.

Week 10's transformer read reviews. Mask it to look only backwards, train it to predict
the next word, and it writes — that is every large language model. This week you build
the smallest possible generator, then put someone else's very large one behind a client
your tests control, and learn the engineering around it: cost, validation, comparison,
and what happens when the text you send it was written by an attacker.

---

## The week

| Day | Folder | What you'll be able to do |
|---|---|---|
| Mon | `day-1/` | Generate reviews from a bigram model with temperature and top-k |
| Tue | `day-2/` | Hold a conversation through `shoplab.llm` and price every turn |
| Wed | `day-3/` | Ask for JSON, validate it with pydantic, and retry with the error |
| Thu | `day-4/` | Compare an LLM with your week 9 model on accuracy, cost and latency |
| Fri | `milestone/` | A reply drafter with a guardrail, and `GUARDRAILS.md` |

---

## The rule from this week on

**Text from a model is untrusted input.** Validate its format, check its content, and
never let it decide anything your own code can decide.

---

## Before Monday

Nothing is required: every test uses a scripted fake model (`SHOPLAB_LLM=fake`, the
default). To try a real model, optional: `pip install anthropic`, an API key in `.env`
(git ignores it), and `SHOPLAB_LLM=anthropic`. A whole week of experiments costs cents.

---

## Outside-view question

> *A ghost-writer drafts a speech for a politician. Whose words are they — and who
> answers for them when one sentence turns out to be false?*
