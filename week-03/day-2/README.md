# Day 2 — Logistic regression, from scratch

> **By the end of today** you can turn a linear model into a probability, train it on log
> loss, and get the same probabilities as scikit-learn.

---

## Read first

- [ ] Google ML Crash Course — [Logistic regression](https://developers.google.com/machine-learning/crash-course/logistic-regression) — all three pages · 25 min
- [ ] scikit-learn — [Logistic regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression) — the first two paragraphs · 5 min

---

## What you need to know

### Squash a line into a probability

Week 2's `X @ w + b` can be any number. The sigmoid, `1 / (1 + e⁻ᶻ)`, squeezes it into
(0, 1). Large positive: nearly certain to leave. Zero: a coin toss.

Write it so it never overflows: `e⁻ᶻ` for z = −1000 is too big for a float. For negative z
use the equal form `eᶻ / (1 + eᶻ)`.

### Log loss

Squared error barely punishes a confident wrong answer. Log loss, `−[y log p + (1 − y) log(1 − p)]`,
punishes it without limit. Its gradient with a sigmoid is the same shape as week 2's:
`Xᵀ(p − y) / n`.

### Did it learn anything?

On the frozen test set your model's log loss is **0.319**. Guessing the training churn
rate (13%) for everyone scores **0.386**. Lower is better, and the gap is what the six
features know.

---

## Exercises

```bash
pytest week-03/day-2 -v
```

Write `sigmoid`, `log_loss` and the class in `logistic.py`.

---

## Predict-then-run

After fitting, look at `model.w_`. Which feature has the largest positive weight? Guess
from week 1's rate-by-bucket plot first.

---

## Before you close the laptop

Commit, push, fill in the signal log.
