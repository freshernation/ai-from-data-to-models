# Day 3 — Move the mug

> **By the end of today** you can show, with two numbers, why a CNN beats a dense
> network on images — even with a twelfth of the weights.

---

## Read first

- [ ] Dive into Deep Learning — [From fully connected layers to convolutions](https://d2l.ai/chapter_convolutional-neural-networks/why-conv.html) — 7.1.1 and 7.1.2 · 20 min

---

## What you need to know

### Two networks, same photos

A dense network flattens the photo to 256 numbers and learns a weight for each pixel:
16,708 weights. The CNN: 1,316. Both are trained on photos with the product near the
centre.

### The finding

| | weights | centred test | moved test |
|---|---|---|---|
| dense | 16,708 | ~100% | **~46%** |
| CNN | 1,316 | ~100% | **~100%** |

The moved test set has products up to three pixels further from the centre than any
training photo. The dense network learned *which pixels light up for a mug*; move the
mug and different pixels light up. The CNN learned *what a mug's edges look like*, and
looks for them everywhere.

### The test set that matters

Both networks are perfect on the test set that looks like the training data. Only a test
set built to differ shows the difference. That is this week's rule.

---

## Exercises

```bash
pytest week-08/day-3 -v
```

Copy `trainer.py` and `cnn.py`, then write `dense_net` and `compare` in `shift_test.py`.

---

## Predict-then-run

Write down your guess for the dense network's accuracy on moved products before running.

---

## Before you close the laptop

Commit, push, fill in the signal log.
