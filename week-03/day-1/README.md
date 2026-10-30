# Day 1 — A split you can trust

> **By the end of today** you can split data into train and test by hand, keep the class
> balance with a stratified split, and name the baseline the test set implies.

---

## Read first

- [ ] Google ML Crash Course — [Dividing the original dataset](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets) · 10 min
- [ ] scikit-learn — [Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html) — the introduction, up to 3.1.1 · 15 min

---

## What you need to know

### Why hold data back

A model scored on the customers it learned from is scored on its memory. Hold a quarter
back, never look at it while building, and score once at the end. That number is the
only one that predicts next month.

### Splits are index arrays

Return positions, not frames: `train_idx, test_idx`. Then `df.iloc[test_idx]` or
`y[test_idx]` works for anything. Seed the random generator so the split is the same
tomorrow.

### An unlucky split moves the target

Twenty random 25% splits of the shop gave test sets whose churn rate ran from **11.2% to
15.2%**. The baseline you must beat moves by four points before any model exists. A
stratified split takes 25% of the leavers and 25% of the stayers separately: 13.0%, every time.

From today the course uses one stratified split, `shoplab.customers.frozen_split()`, for
everything. Nobody re-splits to get a better number.

---

## Exercises

```bash
pytest week-03/day-1 -v
```

Write the four functions in `split.py`.

---

## Predict-then-run

How many churners land in a stratified 25% test set of the shop's 2,000 customers?
Compute it before running `frozen_split()`.

---

## Before you close the laptop

Commit, push, fill in the signal log.
