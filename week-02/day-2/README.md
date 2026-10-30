# Day 2 — Slopes, and walking downhill

> **By the end of today** you can compute a derivative two ways, check one against the
> other, and predict whether a learning rate converges.

---

## Read first

- [ ] Dive into Deep Learning — [Calculus](https://d2l.ai/chapter_preliminaries/calculus.html) — sections 2.4.1 and 2.4.3 · 20 min
- [ ] Google ML Crash Course — [Gradient descent](https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent) · 15 min

---

## What you need to know

### A derivative is a slope you can measure

Nudge `x` a tiny amount each way and see how much `f` changes:
`(f(x + h) - f(x - h)) / 2h`. That is the **finite difference**. It is slow but needs no
formula, which makes it the perfect check for a formula you derived.

### The gradient of the error

For a linear model, the mean squared error's gradient is `2/n · Xᵀ(Xw + b − y)` for the
weights, `2/n · Σ(Xw + b − y)` for the bias. Your tests compare it, weight by weight,
against the finite difference.

### Gradient descent, and the one number that decides it

Step against the slope: `x ← x − lr · grad(x)`. On x² from 1:

| lr | after 20 steps |
|---|---|
| 0.1 | 0.0115 — almost at the bottom |
| 1.0 | 1.0 — jumps across the valley forever |
| 1.1 | 38.3 — every jump overshoots further |

Too small is slow. Too big never arrives, or explodes.

---

## Exercises

```bash
pytest week-02/day-2 -v
```

Write the four functions in `gradients.py`.

---

## Predict-then-run

What does lr 0.5 do on x²? Work out one step by hand, then run it.

---

## Before you close the laptop

Commit, push, fill in the signal log.
