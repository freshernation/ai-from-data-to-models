# Day 3 — Customers who bought this also bought

> **By the end of today** you can build a purchase matrix, compute item-to-item cosine
> similarity, and recommend items a customer has not bought.

---

## Read first

- [ ] Google — [Recommendation systems: collaborative filtering](https://developers.google.com/machine-learning/recommendation/collaborative/basics) · 15 min
- [ ] Google — [Candidate generation](https://developers.google.com/machine-learning/recommendation/overview/candidate-generation) · 10 min

---

## What you need to know

### The matrix

One row per customer, one column per item, 1 where they bought it. 2,000 × 60. Every
column is an item described by who bought it.

### Cosine similarity

Two items are similar when the same customers bought both. Divide each column by its
length; then column `i` dotted with column `j` is their cosine: 1 if exactly the same
buyers, 0 if none in common. One matrix product gives all 60 × 60 at once.

### Recommend

A customer's row times the similarity matrix scores every item by how similar it is to
what they own. Drop what they already have; take the top k. Customer C00001 bought I001,
I002 and I011; their top suggestion is I003, the item I002's buyers buy next.

---

## Exercises

```bash
pytest week-05/day-3 -v
```

Write the four functions in `recommend.py`.

---

## Predict-then-run

Which item will be most similar to I001? Look at what C00001 bought first.

---

## Before you close the laptop

Commit, push, fill in the signal log.
