# Day 1 — An image is an array; a filter slides over it

> **By the end of today** you can convolve and pool an image by hand, match PyTorch's
> answer, and show that moving the photo moves the features with it.

---

## Read first

- [ ] Dive into Deep Learning — [Convolutions for images](https://d2l.ai/chapter_convolutional-neural-networks/conv-layer.html) — 7.2.1 to 7.2.3 · 20 min
- [ ] Stanford CS231n — [Convolutional networks](https://cs231n.github.io/convolutional-networks/) — "Convolutional layer", the overview and the demo · 15 min

---

## What you need to know

### A photo is a grid of numbers

`shoplab.images.load()["X_train"][0]` is a 16 × 16 array of brightnesses, 0 to 255.
Print it with `#` for bright pixels and you can see the mug.

### Convolution

Lay a small kernel (3 × 3) on the image, multiply overlapping numbers, add them up: one
output number. Slide one pixel; repeat. The edge kernel — 8 in the middle, −1 around —
is zero on flat areas and large where brightness changes: it draws the outline. A 16 × 16
image and a 3 × 3 kernel give 14 × 14.

### The same filter everywhere

Move the photo two pixels down and one right, then convolve: you get exactly the
convolved original, moved two down and one right. The filter does not care where the
mug is. That one property is why CNNs beat dense networks on images — Wednesday measures it.

### Pooling

Max pooling keeps the largest value in each 2 × 2 block: half the size, and a feature
that moved by one pixel often lands in the same block.

---

## Exercises

```bash
pytest week-08/day-1 -v
```

Write `convolve2d`, `max_pool` and `shift` in `convolve.py`. Then save a plot of a photo
and its edge map side by side.

---

## Predict-then-run

Before convolving: what does the edge kernel output on a patch of all-black pixels? On
all-white?

---

## Before you close the laptop

Commit, push, fill in the signal log.
