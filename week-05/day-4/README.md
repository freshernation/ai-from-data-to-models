# Day 4 — Did it recommend anything?

> **By the end of today** you can hide each customer's last purchase, rebuild the
> recommender without it, and measure how often the hidden item comes back.

---

## Read first

- [ ] Google — [Recommendation systems: overview](https://developers.google.com/machine-learning/recommendation/overview/types) · 10 min
- [ ] scikit-learn — [Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) — re-read "Data leakage": it applies with no labels too · 5 min

---

## What you need to know

### Hide something you know

There is no label, but there is time: every purchase has a `seq`. Hold back each
customer's last purchase, build the matrix from the rest, recommend, and see whether the
held-back item is in the list.

### Hit rate at k

The fraction of customers whose hidden item appears in their top k. It is crude — it
ignores order and anything bought later — but it is honest, and it has a baseline.

### The finding

| | top 10 | top 5 |
|---|---|---|
| Item-item | **73.3%** | **52.7%** |
| Most popular | 31.3% | 17.0% |

Counting co-purchases more than doubles the baseline, and nothing was learned at all.

---

## Exercises

```bash
pytest week-05/day-4 -v
```

Copy `recommend.py` from day 3, then write `evaluate_recs.py`.

---

## Predict-then-run

If you built the matrix from all orders instead of history, what would the hit rate be?
Write a number, then try it — and then put it back.

---

## Before you close the laptop

Commit, push, fill in the signal log. Then start the milestone.
