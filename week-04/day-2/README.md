# Day 2 — Memorising, and voting

> **By the end of today** you can show a tree overfitting with two columns of numbers,
> and score a random forest and gradient boosting against week 3's line.

---

## Read first

- [ ] Google ML Crash Course — [Overfitting](https://developers.google.com/machine-learning/crash-course/overfitting/overfitting) · 10 min
- [ ] scikit-learn — [Ensembles: forests and boosting](https://scikit-learn.org/stable/modules/ensemble.html) — the introductions to "Gradient-boosted trees" and "Random forests" · 20 min

---

## What you need to know

### A deep tree memorises

Keep splitting and every leaf ends up holding one customer. Training AUC: **1.0**. On new
customers the tree peaks at depth 5 (**0.691**) and falls to **0.653** unlimited. The
distance between the training and test columns is overfitting, measured.

### Forests and boosting

A **random forest** grows hundreds of deep trees, each on a random sample of rows and
columns, and averages them: the memorised noise cancels out. **Gradient boosting** grows
small trees one after another, each correcting the last one's errors.

### The finding

Forest: 0.968 on training data, **0.765** on test. Boosting: **0.777**. Week 3's logistic
regression: **0.779**. The line wins. The shop's churn is close to a weighted sum of its
columns, and a line is exactly that shape. Tomorrow you learn to find this out without
looking at the test set — today you looked, so that you believe tomorrow's method.

---

## Exercises

```bash
pytest week-04/day-2 -v
```

Write the four functions in `ensembles.py`.

---

## Predict-then-run

Before running: will the forest's *training* AUC be closer to the deep tree's 1.0 or to
its test AUC?

---

## Before you close the laptop

Commit, push, fill in the signal log.
