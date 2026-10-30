# Day 1 — Vectors, matrices, and a model that is a weighted sum

> **By the end of today** you can multiply two matrices with loops, explain what `@`
> does, and write any linear model as `X @ w + b`.

---

## Read first

- [ ] 3Blue1Brown — [Essence of linear algebra](https://www.3blue1brown.com/topics/linear-algebra) — chapters 1 and 4 · 25 min
- [ ] NumPy — [`numpy.matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html) — the description and the first examples · 5 min

---

## What you need to know

### A dot product is a weighted sum

`dot([2, 10], [4.5, 0.3]) = 2*4.5 + 10*0.3 = 12`. Weights times features, added up.
That is the heart of every model in this course, up to the transformer.

### A matrix product is many dot products

Row `i` of `A` dotted with column `j` of `B` gives entry `(i, j)`. An `(n, k)` times a
`(k, m)` is `(n, m)`: the inner sizes must match and disappear. Say the shapes aloud
before you multiply.

### A table of customers times a weight vector is a column of predictions

`X` has one row per customer, one column per feature: shape `(n, k)`. `w` has one weight
per feature: shape `(k,)`. `X @ w + b` gives `n` predictions in one line. The shop's spend
formula, 12 + 4.5 × orders + 0.3 × tenure, is a linear model whose weights someone
typed in. On Thursday the computer finds them from the data.

---

## Exercises

```bash
pytest week-02/day-1 -v
```

`dot` and `matmul` with loops and lists, no numpy. Then `predict` and `predicted_spend` with numpy.

---

## Predict-then-run

What shape is `X @ w` when `X` is `(2000, 2)` and `w` is `(2,)`? Write it down, then check.

---

## Before you close the laptop

Commit, push, fill in the signal log.
