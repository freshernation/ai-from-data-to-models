# Day 2 — Forwards through two layers

> **By the end of today** you can compute a two-layer network's probabilities in numpy,
> with every shape named, and solve XOR with weights you set yourself.

---

## Read first

- [ ] Dive into Deep Learning — [Softmax regression](https://d2l.ai/chapter_linear-classification/softmax-regression.html) — 4.1.1 to 4.1.2 · 20 min
- [ ] Dive into Deep Learning — [Multilayer perceptrons](https://d2l.ai/chapter_multilayer-perceptrons/mlp.html) — 5.1.2 "Activation functions", relu only · 10 min

---

## What you need to know

### The shapes

`X (n, d) → z1 = X @ W1 + b1 (n, hidden) → h = relu(z1) → logits = h @ W2 + b2 (n, classes) → softmax`.
Say each shape aloud. Every bug this week is a shape you did not say.

### relu and softmax

relu keeps positives and zeros negatives: it is what lets two layers bend. Softmax turns a
row of scores into probabilities that add to 1. Subtract the row's max first, or `exp(1000)`
overflows; the shift cancels out.

### Cross-entropy

The loss is `−log` of the probability the network gave the right class, averaged. Week 3's
log loss, for any number of classes.

### XOR by hand

Two hidden units: one counts the 1s, one fires only when both are 1. The output says
"yes" for the first and "no" for the second. The test sets those weights and your forward
pass gets XOR right. Two layers do what one could not.

---

## Exercises

```bash
pytest week-06/day-2 -v
```

Write the five functions in `forward.py`. Keep the cache: tomorrow needs it.

---

## Predict-then-run

With `init_params(2, 8, 2, seed=0)` and no training, what accuracy will XOR get? Why is
"about 50%" the right guess?

---

## Before you close the laptop

Commit, push, fill in the signal log.
