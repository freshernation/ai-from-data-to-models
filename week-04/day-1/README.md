# Day 1 — One question, chosen by hand

> **By the end of today** you can measure how mixed a group is, find the single question
> that separates leavers from stayers best, and match scikit-learn's choice.

---

## Read first

- [ ] Google — [Decision forests: decision trees](https://developers.google.com/machine-learning/decision-forests) — "Decision trees" and "Growing decision trees" · 25 min
- [ ] scikit-learn — [Decision trees](https://scikit-learn.org/stable/modules/tree.html) — "Classification" and "Tips on practical use" · 10 min

---

## What you need to know

### Impurity

Gini impurity is `1 − Σ pₖ²`: the chance two customers drawn at random from a group have
different labels. All stayers: 0. Half and half: 0.5.

### A split is a question

"Is `days_since_last_order` ≤ 75.5?" divides the customers in two. Its **gain** is the
impurity before, minus the size-weighted impurity of the two halves. Try every column and
every midpoint between neighbouring values; keep the largest gain.

### The finding

On the training customers the best first question is **silent for more than 75.5 days?**
Yes: 60.5% leave. No: 10.5%. The same signal you plotted in week 1, found by brute force.
scikit-learn's tree asks exactly the same question. A tree is this, repeated on each half.

---

## Exercises

```bash
pytest week-04/day-1 -v
```

Write `gini`, `split_gain`, `best_split` and `Stump` in `tree.py`.

---

## Predict-then-run

Which column do you expect the first split to use, and roughly where? You have a plot
from week 1 that answers it.

---

## Before you close the laptop

Commit, push, fill in the signal log.
