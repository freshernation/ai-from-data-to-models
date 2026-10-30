# Day 1 — Attention by hand

> **By the end of today** you can compute attention for a batch of sequences in numpy,
> mask out what a word may not see, and match PyTorch exactly.

---

## Read first

- [ ] Jay Alammar — [The illustrated transformer](https://jalammar.github.io/illustrated-transformer/) — up to "Matrix calculation of self-attention" · 25 min
- [ ] Dive into Deep Learning — [Attention scoring functions](https://d2l.ai/chapter_attention-mechanisms-and-transformers/attention-scoring-functions.html) — 11.3.2 and 11.3.3 · 15 min

---

## What you need to know

### Query, key, value

Each word asks a question (its **query**), advertises what it holds (its **key**) and
offers content (its **value**). A word's output is the average of every value, weighted
by how well its query matches each key: `softmax(Q Kᵀ / √d) V`. Week 5's dot-product
similarity, used to decide where to look.

### Why √d

Dot products of long vectors are large; softmax of large numbers is nearly all-or-nothing
and its gradient vanishes. Dividing by √d keeps the scores in a range softmax can learn from.

### Masks

Set a score to −∞ and its weight becomes exactly 0: that word is not looked at. Two masks
matter: one that hides padding, and one that hides every later word. With the second, the
first word can only look at itself — and that is the whole difference between this week's
encoder and next week's generator.

---

## Exercises

```bash
pytest week-10/day-1 -v
```

Write `softmax`, `attention` and `self_attention` in `attention.py`.

---

## Predict-then-run

With one query and one key, what are the weights, whatever the numbers? Write it down,
then run the first test.

---

## Before you close the laptop

Commit, push, fill in the signal log.
