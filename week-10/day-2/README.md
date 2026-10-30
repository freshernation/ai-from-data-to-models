# Day 2 — Where is each word?

> **By the end of today** you can prove attention cannot see order, and give it order
> with a position code.

---

## Read first

- [ ] Dive into Deep Learning — [Self-attention and positional encoding](https://d2l.ai/chapter_attention-mechanisms-and-transformers/self-attention-and-positional-encoding.html) — 11.6.1 and 11.6.3 · 20 min
- [ ] Vaswani et al. — [Attention is all you need](https://arxiv.org/abs/1706.03762) — section 3.5 only (open the PDF) · 5 min

---

## What you need to know

### Attention is a set operation

Every word is compared with every word; nothing says which came first. Reverse the
sentence and each output moves with its word — so the average over the sentence is
**identical**, to rounding (a difference of about 2e-16). To plain attention, "not good,
bad" and "bad, not good" are the same sentence.

### A position code

Add to each word's vector a pattern that depends only on its position: sines and cosines
at different speeds, one pair per two dimensions. Now the same word at position 1 and
position 4 is two different vectors, and the reversed sentence pools to something
different (a gap of about 0.1 in the test).

### Whether you need it

That depends on the data. Tomorrow you train a transformer with and without the code
and find out what the shop's reviews need.

---

## Exercises

```bash
pytest week-10/day-2 -v
```

Copy `attention.py`, then write `sinusoidal`, `pooled` and `order_gap` in `position.py`.

---

## Predict-then-run

Plot `sinusoidal(32, 32)` as an image. Which columns change fastest down the rows?

---

## Before you close the laptop

Commit, push, fill in the signal log.
