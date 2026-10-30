# Day 2 — Module, loader, loop

> **By the end of today** you can write a network as an `nn.Module`, feed it with a
> `DataLoader`, and train it with an optimiser in the loop every PyTorch project uses.

---

## Read first

- [ ] PyTorch — [Datasets and DataLoaders](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html) — up to "Preparing your data for training" · 10 min
- [ ] PyTorch — [Build the neural network](https://docs.pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html) · 10 min
- [ ] PyTorch — [Optimizing model parameters](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) — "Optimization loop" · 10 min

---

## What you need to know

### The loop, in four lines

```python
optimiser.zero_grad()      # forget last step's gradients
loss = loss_fn(model(xb), yb)
loss.backward()            # compute this step's
optimiser.step()           # move every parameter
```

Forget `zero_grad()` and gradients add up across steps. It runs; it trains badly.

### Mini-batches

A `DataLoader` serves the data in shuffled batches. One pass over all of it is an
**epoch**. With batches of 32, one epoch of 450 points is 15 steps instead of one.

### The finding

The same 100 epochs on the moons: the full batch takes 100 steps and reaches about
**90%**; batches of 32 take 1,500 noisier steps and reach about **92%**. Each step sees
less, but there are fifteen times as many.

---

## Exercises

```bash
pytest week-07/day-2 -v
```

Write `make_loader`, `Net`, `train` and `accuracy` in `loop.py`.

---

## Predict-then-run

How many parameters does `Net(2, 16, 2)` have? Count before you run `sum(p.numel() ...)`.

---

## Before you close the laptop

Commit, push, fill in the signal log.
