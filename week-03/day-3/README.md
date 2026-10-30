# Day 3 — What accuracy hides

> **By the end of today** you can build a confusion matrix and compute precision, recall,
> F1 and ROC AUC by hand — and say which one the shop cares about.

---

## Read first

- [ ] Google ML Crash Course — [Accuracy, precision, recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall) · 15 min
- [ ] Google ML Crash Course — [ROC and AUC](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc) · 10 min

---

## What you need to know

### Four boxes

Every prediction lands in one: true positive (flagged, left), false positive (flagged,
stayed), true negative, false negative (missed, left). Every metric is a ratio of boxes.

- **Precision**: of those flagged, how many left? Wasted offers lower it.
- **Recall**: of those who left, how many were flagged? Missed leavers lower it.
- **F1**: one number that is high only if both are.

### AUC: ranking, not deciding

AUC ignores the threshold. It asks: pick a random leaver and a random stayer — how
often does the leaver score higher? 0.5 is a coin; 1.0 is perfect.

### The finding

At 0.5, logistic regression is **88.8%** accurate against an **87.0%** baseline. Under two
points. Its confusion matrix: 18 leavers caught, 47 missed. Recall **27.7%**. The AUC is
**0.78**: it ranks customers well, but 0.5 is the wrong place to cut. That is tomorrow.

---

## Exercises

```bash
pytest week-03/day-3 -v
```

Write the five functions in `metrics.py`, by hand.

---

## Predict-then-run

What is the recall of "nobody leaves"? Its precision? Its accuracy? Write all three down.

---

## Before you close the laptop

Commit, push, fill in the signal log.
