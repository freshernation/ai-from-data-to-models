# Day 3 — Bigger than its data

> **By the end of today** you can show a network memorising sixty points, and compare
> three ways to stop it by what they do to the validation curve.

---

## Read first

- [ ] Dive into Deep Learning — [Weight decay](https://d2l.ai/chapter_linear-regression/weight-decay.html) — 3.7.1 · 10 min
- [ ] Dive into Deep Learning — [Dropout](https://d2l.ai/chapter_multilayer-perceptrons/dropout.html) — 5.6.1 to 5.6.2 · 15 min

---

## What you need to know

### Memorising, measured

Sixty training points, a network with 66,000 weights, 300 epochs of Adam. Training loss
reaches **0.000**. Validation loss is best at about epoch **13** (0.27) and then climbs to
about **3.8**. Yet validation accuracy falls only from about 88% to 85%: the network gets
more and more *confident* about the same mistakes. Loss sees memorising before accuracy does.

### Three cures

| | how it works | validation loss at the end | accuracy |
|---|---|---|---|
| none | — | ~3.8 | ~85% |
| early stopping | keep the best epoch's weights | ~0.27 | ~88% |
| dropout 0.5 | randomly silence half the units while training | ~1.2 | ~87% |
| weight decay 0.05 | pull every weight towards zero each step | ~0.37 | ~85% |

(Measured on torch 2.2; other versions land close, not exact.) Weight decay stops the
climb; early stopping gives the best accuracy here; they combine.

### `train()` and `eval()`

Dropout must be off when measuring. `model.eval()` turns it off; `model.train()` turns
it back on. Forget it and your validation numbers are noisy and too low.

---

## Exercises

```bash
pytest week-07/day-3 -v
```

Write `big_net`, `fit_curves`, `accuracy` and `compare` in `regularise.py`. Then plot
`train_losses` and `val_losses` for "none" and save the PNG.

---

## Predict-then-run

Before running: at which epoch, roughly, will validation loss be lowest — 10, 100 or 300?

---

## Before you close the laptop

Commit, push, fill in the signal log.
