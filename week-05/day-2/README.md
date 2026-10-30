# Day 2 — Six columns on one page

> **By the end of today** you can find the directions along which customers differ most,
> with one SVD, and project every customer onto two of them.

---

## Read first

- [ ] scikit-learn — [Principal component analysis](https://scikit-learn.org/stable/modules/decomposition.html#pca) — the first section · 10 min
- [ ] Shlens — [A tutorial on principal component analysis](https://arxiv.org/abs/1404.1100) — sections I to III (open the PDF) · 25 min

---

## What you need to know

### Centre, then decompose

Subtract each column's mean. `np.linalg.svd` splits the centred table into directions
(the rows of `Vt`), each with a strength (`s`). The first direction is the one along which
customers vary most; each next one is at right angles to those before it.

### Explained variance

`s²` divided by the total says how much of the spread each direction holds. On the shop's
category shares, the first two hold **33%** and **29%**: **62%** of how 2,000 customers
differ, in two numbers each. Plot them and the three groups are three clouds, with the
browsers smeared between them.

### Sign does not matter

A direction and its negative are the same axis. Your components may point the opposite
way to scikit-learn's; the tests compare absolute values.

---

## Exercises

```bash
pytest week-05/day-2 -v
```

Write `pca` in `pca.py`. Then plot `projected` coloured by Monday's clusters and save it.

---

## Predict-then-run

Six categories, but the shares always add up to 1. How many directions can have any
variance at all? Check `s` after you write it.

---

## Before you close the laptop

Commit, push, fill in the signal log.
