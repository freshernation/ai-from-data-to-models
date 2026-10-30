# Day 1 — Grouping customers with no labels

> **By the end of today** you can write k-means, read an elbow curve, and say why the
> number it suggests is not always the number of kinds of customer.

---

## Read first

- [ ] Google — [Clustering: k-means](https://developers.google.com/machine-learning/clustering) — "What is clustering?" and "k-means" · 20 min
- [ ] scikit-learn — [K-means](https://scikit-learn.org/stable/modules/clustering.html#k-means) — the first four paragraphs · 10 min

---

## What you need to know

### Describe each customer the same way

`shoplab.orders.category_shares()` gives every customer six numbers: the share of their
purchases in kitchen, garden, books, toys, sports and beauty. Two customers with similar
shares buy similarly, whatever they spend.

### k-means in two lines

Put each customer with the nearest centroid. Move each centroid to the mean of its
customers. Repeat until nothing moves. The answer depends on where the centroids start,
so run it ten times and keep the run with the lowest **inertia** (total squared distance).

### The elbow, and what it cannot see

Inertia always falls as k grows. Look for the bend: 672 → 488 → 327, then 270, 223, 182.
The elbow is at **3**. The shop was generated with **four** segments — but the fourth,
browsers who buy evenly from everything, sits in the middle of the other three. There is
no cloud for a centroid to find. Against the hidden answer key, three clusters are
**78%** pure. A clustering finds shapes, not truths.

---

## Exercises

```bash
pytest week-05/day-1 -v
```

Write the six functions in `kmeans.py`. `shoplab.orders.hidden_segments()` exists for the
tests; do not read it in your code.

---

## Predict-then-run

Before running the elbow: how many segments would you guess from the six categories?

---

## Before you close the laptop

Commit, push, fill in the signal log.
