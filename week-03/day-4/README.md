# Day 4 — A threshold chosen with money

> **By the end of today** you can price every mistake, find the threshold that makes the
> most money, and explain why it is nowhere near 0.5.

---

## Read first

- [ ] Google ML Crash Course — [Thresholds and the confusion matrix](https://developers.google.com/machine-learning/crash-course/classification/thresholding) · 10 min
- [ ] scikit-learn — [Tuning the decision threshold](https://scikit-learn.org/stable/modules/classification_threshold.html) — the introduction · 10 min

---

## What you need to know

### A mistake has a price

A retention offer costs **10**. A customer who leaves is worth **200** a year, and an
offer keeps 30% of them: a flagged leaver is worth 60 on average. Missing a leaver costs
six times as much as a wasted offer.

### The best threshold

Try 0.05, 0.10, … 0.95 on the training scores and keep the one that makes the most:
**0.10**. On the test set it makes **1,090**; at 0.5 the same model makes **810**. Offer
everyone and you lose 1,100.

At 0.10 the model's accuracy falls to **71.2%**, below the 87% baseline. It flags 173
customers to catch 47 leavers. Accuracy got worse, the business got better. Which number
to optimise was never a technical question.

### Choose on training data

The threshold is a setting you learned. Learn it on training data, or the test score is
flattering you.

---

## Exercises

```bash
pytest week-03/day-4 -v
```

Write `value` and `best_threshold` in `thresholds.py`.

---

## Predict-then-run

If an offer saved 10% of leavers instead of 30%, would the best threshold go up or down?

---

## Before you close the laptop

Commit, push, fill in the signal log. Then start the milestone.
