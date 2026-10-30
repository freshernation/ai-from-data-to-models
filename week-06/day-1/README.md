# Day 1 — The perceptron, and XOR

> **By the end of today** you can train the oldest neural network there is, and show the
> problem it can never solve.

---

## Read first

- [ ] 3Blue1Brown — [Neural networks, chapter 1](https://www.3blue1brown.com/topics/neural-networks) — "But what is a neural network?" · 20 min
- [ ] Dive into Deep Learning — [Multilayer perceptrons](https://d2l.ai/chapter_multilayer-perceptrons/mlp.html) — 5.1.1 "Hidden layers" · 10 min

---

## What you need to know

### A perceptron is week 3's model with a hard step

`step(x @ w + b)`: 1 or 0. Its learning rule is simple: when wrong, move the weights
towards the right answer by `lr × error × x`. For AND and OR it gets everything right
within five epochs.

### A line cannot do XOR

XOR is 1 when exactly one input is 1. Plot the four points: the 1s sit on opposite corners.
No straight line puts both on one side. In a hundred epochs the perceptron never scores
better than **50%** on XOR — a coin.

### What fixes it

A hidden layer: first compute some new features of the input, then draw a line through
those. Tomorrow you set such weights by hand; on Thursday the network finds them itself.

---

## Exercises

```bash
pytest week-06/day-1 -v
```

Write `step` and `Perceptron` in `perceptron.py`.

---

## Predict-then-run

Draw the four XOR points. Draw the best line you can. What accuracy does it get? That is
the best any perceptron could ever do — and yours will do worse. Why?

---

## Before you close the laptop

Commit, push, fill in the signal log.
