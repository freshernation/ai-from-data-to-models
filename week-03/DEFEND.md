# Week 3 — Friday defence

Forty minutes. It starts with `python churn_v1.py`, run live.

---

## Phase 0 — Live (5 min)

Run `python week-03/milestone/churn_v1.py`. Read out the accuracy, the baseline, the
recall and the value.

## Phase 1 — Explain (10 min)

1. *"Your model is less accurate than predicting nobody leaves. Why ship it?"* — It finds 47 of 65 leavers and makes 1,090 against 810 at 0.5; accuracy treats a missed leaver and a wasted offer as equal, and they are not. The best question of the week.
2. *"Why was the threshold chosen on training data?"* — Choosing it on the test set makes the test set part of training; the reported number would be optimistic.
3. *"What does an AUC of 0.78 mean, in a sentence?"* — Pick a random leaver and a random stayer: 78% of the time the leaver scores higher.
4. *"Why log loss and not squared error?"* — It punishes confident wrong answers hard, and with a sigmoid its gradient is the same simple `error × x`.
5. *"Why stratify?"* — With 13% positives, a random 500 can hold 11% or 15%, moving the baseline before any model exists.

## Phase 2 — Mutate (10 min)

- *"The offer now costs 30."* — One constant; predict whether the threshold goes up or down before running.
- *"Report F1 too."* — Which file, which line.

## Phase 3 — Debug (10 min)

| Seed | Break | Probes |
|---|---|---|
| Easy | `predict` uses `>` instead of `>=` | Do the tests catch a boundary? |
| Medium | `fit` standardises, `predict_proba` does not | Probabilities near 0 or 1 everywhere |
| Medium | precision and recall swapped | Numbers plausible; do they check against the confusion matrix? |
| Nasty | `train()` picks the threshold on the test scores | No error; value goes *up* slightly; the evaluation is now a lie |

The **Nasty** one: the most dangerous bug in machine learning makes your numbers better.

---

## Scoring

| Phase | 5 | 3 | 1 |
|---|---|---|---|
| **Live** | Runs; explains every number | Runs | Does not run |
| **Explain** | Costs and leakage in their own words | Needs prompting | Recites |
| **Mutate** | Predicts the direction, then names every line | Gets there | Cannot place the change |
| **Debug** | Suspects the silent one | Finds it | Guesses |

---

## Instructor: framing week 4

> **A straight line can only say "more tickets, more risk".** Next week the model asks
> questions — "silent for 60 days? then: on basic?" — and a hundred of them vote. It is the
> strongest model there is for tables like ours, and the easiest to fool yourself with.
