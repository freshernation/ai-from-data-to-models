# Day 1 — Forty lines become one call

> **By the end of today** you can write week 6's network as torch tensors and get every
> gradient from `loss.backward()` — and say why float32 disagrees in the eighth decimal.

---

## Read first

- [ ] PyTorch — [Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html) · 15 min
- [ ] PyTorch — [Automatic differentiation](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html) · 15 min

---

## What you need to know

### A tensor is an array that remembers

`torch.tensor(W, requires_grad=True)` is a numpy array that records every operation done
with it. Compute the loss; call `loss.backward()`; every tensor's `.grad` now holds the
gradient. It is the chain rule you wrote on Wednesday, applied automatically.

### Cross-entropy takes logits

`F.cross_entropy(logits, y)` applies softmax itself, in a numerically safe way. Give it
the raw scores, never probabilities.

### float32

In float64, autograd and your week-6 backprop agree to **1e-16**. In float32, PyTorch's
default, they differ by about **1e-8** — not a bug: float32 keeps about seven significant
digits. Every network from now on trains in float32, because it is twice as fast and the
eighth digit never mattered.

---

## Exercises

```bash
pytest week-07/day-1 -v
```

Write the three functions in `autograd.py`.

---

## Predict-then-run

Before running: in float32, which will be further from your hand-written gradients —
W1 or b2? Why might it differ?

---

## Before you close the laptop

Commit, push, fill in the signal log.
