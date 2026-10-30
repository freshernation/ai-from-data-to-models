# Day 3 — Is the world still the same?

> **By the end of today** you can measure drift between two months of customers, report
> a fairness number with the count it rests on, and explain one prediction exactly.

---

## Read first

- [ ] Chip Huyen — [Data distribution shifts and monitoring](https://huyenchip.com/2022/02/07/data-distribution-shifts-and-monitoring.html) — sections 1 and 2 · 25 min
- [ ] Google ML Crash Course — [Fairness](https://developers.google.com/machine-learning/crash-course/fairness) — "Types of bias" and "Evaluating for bias" · 15 min

---

## What you need to know

### PSI

Cut last month's values into ten equal-sized bins. Count what share of this month falls
in each. The population stability index adds up how far the shares moved: below 0.1
stable, 0.1 to 0.25 watch, above 0.25 drifted.

### The finding

`shoplab.customers.next_month()` is a month after a reminder email went to silent
customers; 70% of them placed a small order. Days since last order: **PSI 0.52**,
drifted. Every other column: below 0.03. And the model, unchanged, now misses leavers —
recall at 0.10 falls from **72% to 49%** (a line on the six columns) while the churn rate
barely moved. The email changed the feature, not who leaves.

### A fairness number needs its count

Recall by plan: pro customers **0%**. There is **one** pro leaver in the test set. Report
the count beside every group's rate, or the rate means nothing.

### Explaining one prediction

For a linear model the explanation is exact: each column's standardised value times its
weight, and the parts add up to the score. Customer C00003 is unlikely to leave mainly
because they ordered yesterday.

---

## Exercises

```bash
pytest week-12/day-3 -v
```

Write the five functions in `monitor.py`.

---

## Predict-then-run

Before running: which column will drift next month, and roughly by how much?

---

## Before you close the laptop

Commit, push, fill in the signal log.
