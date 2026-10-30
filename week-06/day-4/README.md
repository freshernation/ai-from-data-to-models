# Day 4 — Training it, and breaking it

> **By the end of today** you can train your network on XOR, and explain two ways to make
> it never learn.

---

## Read first

- [ ] Dive into Deep Learning — [Numerical stability and initialisation](https://d2l.ai/chapter_multilayer-perceptrons/numerical-stability-and-init.html) — 5.4.1 and 5.4.2 · 20 min
- [ ] Andrej Karpathy — [A recipe for training neural networks](http://karpathy.github.io/2019/04/25/recipe/) — "The recipe", steps 1 and 2 · 15 min

---

## What you need to know

### The loop

Forward, record the loss, backward, step every parameter against its gradient. Two
thousand times. That is all training is.

### Starting at zero never starts

With every weight zero, every hidden unit outputs zero, relu passes no gradient back, and
nothing moves: the loss sits at **0.6931** (ln 2, a coin) for all 2,000 steps. Random
starting weights, scaled by `√(2 / inputs)` (He initialisation), break the deadlock: five
out of five seeds reach **100%** on XOR.

### The step size window

| lr | after 2,000 steps |
|---|---|
| 0.01 | right answers, loss still 0.165 |
| 0.5 | right answers, loss 0.0004 |
| 5 | stuck at 50% |

Week 2's parabola, again — now with a network that cannot always climb back.

---

## Exercises

```bash
pytest week-06/day-4 -v
```

Copy `forward.py` and `backprop.py`, then write `train` and `accuracy` in `train_mlp.py`.

---

## Predict-then-run

Before running with `scheme="zeros"`, write down the first loss to four decimal places.

---

## Before you close the laptop

Commit, push, fill in the signal log. Then start the milestone.
