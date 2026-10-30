# Day 2 — A small CNN

> **By the end of today** you can build a CNN in PyTorch, count its weights by hand, and
> train it on the shop's product photos with your week 7 trainer.

---

## Read first

- [ ] PyTorch — [`nn.Conv2d`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html) — the description and "Shape" · 10 min
- [ ] Dive into Deep Learning — [Pooling](https://d2l.ai/chapter_convolutional-neural-networks/pooling.html) — 7.5.1 · 10 min

---

## What you need to know

### Channels

`Conv2d(1, 8, 3)` learns eight 3 × 3 filters on a one-channel (grey) image: eight
feature maps out. `Conv2d(8, 16, 3)` learns sixteen filters, each looking at all eight
maps. Input shape `(batch, channels, height, width)`: `as_float` adds the channel axis.

### The network

Conv 8 → ReLU → MaxPool → Conv 16 → ReLU → the **maximum** of each of the 16 maps over
the whole image → Linear to 4 classes. That last max says "did this feature appear
anywhere?" and throws away *where*. Count the weights: 8 × (9 + 1) + 16 × (8 × 9 + 1) +
16 × 4 + 4 = **1,316**.

### Training

Copy week 7's `trainer.py`. 80 epochs at lr 0.03, early stopping on a validation slice:
about four seconds on a laptop, and near-perfect accuracy on the test photos.

---

## Exercises

```bash
pytest week-08/day-2 -v
```

Copy `trainer.py`, then write `SmallCNN`, `split_validation`, `train_model` and
`accuracy` in `cnn.py`.

---

## Predict-then-run

What shape comes out of `features` for a batch of 5? Work it out from the layers, then
check.

---

## Before you close the laptop

Commit, push, fill in the signal log.
