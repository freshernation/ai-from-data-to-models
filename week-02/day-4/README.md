# Day 4 — Fitting a line, two ways

> **By the end of today** you can fit a linear regression exactly and by gradient
> descent, get the same answer, and explain why scaling the features matters.

---

## Read first

- [ ] Google ML Crash Course — [Linear regression](https://developers.google.com/machine-learning/crash-course/linear-regression) — "Loss" and "Hyperparameters" pages · 20 min
- [ ] scikit-learn — [Ordinary least squares](https://scikit-learn.org/stable/modules/linear_model.html) — section 1.1.1 only · 10 min

---

## What you need to know

### The exact way

Add a column of ones (for the bias), then solve `(XᵀX) θ = Xᵀy`. One line with
`np.linalg.solve`. Exact, and fine for a few thousand rows and a few columns.

### The walking way

Start from zero, step against yesterday's gradient until it is nearly flat. Slower here,
but it is the only way that works for a neural network, so it is the one to understand.

### Scale

Tenure runs to 60; orders sit around 3. One learning rate has to suit both weights. On
the raw columns, lr 0.001 diverges and lr 0.0005 needs **58,384** steps. Standardise each
column (subtract its mean, divide by its standard deviation) and lr 0.1 gets there in
**52**. Same answer, a thousand times fewer steps.

---

## Exercises

```bash
pytest week-02/day-4 -v
```

Write the four functions in `regression.py`. The finding test takes a few seconds:
it really runs 58,384 steps.

---

## Predict-then-run

The data was generated with 4.5 per order. Before fitting, predict what weight your
model will give orders. Then fit it, and keep the surprise for Friday.

---

## Before you close the laptop

Commit, push, fill in the signal log. Then start the milestone.
