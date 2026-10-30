# Week 4 — Friday defence

Forty minutes. It starts with `python churn_model.py` on a fresh clone, then the saved
model loaded in a new Python session.

---

## Phase 0 — Live (5 min)

Run `python week-04/milestone/churn_model.py`. Then, in a fresh `python`, load
`churn_model.joblib` and score one customer the instructor makes up on the spot.

## Phase 1 — Explain (10 min)

1. *"Trees are supposed to win on tables. Why did you ship a line?"* — Cross-validation on training data said 0.835 vs 0.813; the data's churn really is close to a weighted sum of its columns. The best question of the week.
2. *"Your unlimited tree scores 1.0 on training data. What does that tell you?"* — Nothing good: it memorised; the test score (0.653) is lower than at depth 5.
3. *"How did 500 columns of noise score 0.74?"* — Columns were chosen using every row's label, including the rows later used to score; selection must happen inside each fold.
4. *"Why do the engineered features barely help?"* — The models already see the raw columns; `silent_60` is a split a tree finds itself, and the line's gain (0.001) is noise.
5. *"What does permutation importance not tell you?"* — Cause. And with correlated columns it splits credit between them.

## Phase 2 — Mutate (10 min)

- *"Add an SVM as a fourth candidate."* — One entry in `candidates()`; what happens to the run time, and why does `predict_proba` need care?
- *"The shop wants the model chosen on F1 at a threshold, not AUC."* — Where, and what else must now be chosen on training data?

## Phase 3 — Debug (10 min)

| Seed | Break | Probes |
|---|---|---|
| Easy | `joblib.load` on a path that does not exist | Reads the error |
| Medium | `candidates()` returns a module-level dict | Same objects refitted; works, but `choose` and `train` share state |
| Medium | `predict_one` forgets `add_features` | KeyError on `spend_per_order` — do they see why? |
| Nasty | `StandardScaler().fit(all_rows)` before `cv_auc`, outside the pipeline | No error; CV numbers move by a hair; the leak is real and invisible |

The **Nasty** one: here the scaler leak barely changes a number, and on Wednesday's
noise the selection leak invented a whole signal. Same bug, different size. You cannot
rely on the number to tell you.

---

## Scoring

| Phase | 5 | 3 | 1 |
|---|---|---|---|
| **Live** | Runs; scores a made-up customer in a fresh session | Runs | Does not run |
| **Explain** | Defends the line with CV numbers | Needs prompting | "Trees always win" |
| **Mutate** | Names every line before typing | Gets there | Cannot place the change |
| **Debug** | Suspects the silent one | Finds it | Guesses |

---

## Instructor: framing week 5

> **Every week so far had an answer column.** Next week it is gone: which customers are
> alike, and what will they buy? No label, no accuracy — so how do you know it worked?
