# Day 3 — Backpropagation

> **By the end of today** you can compute the gradient of the loss for every weight in
> the network by hand, and prove it right with finite differences.

---

## Read first

- [ ] 3Blue1Brown — [Backpropagation calculus](https://www.3blue1brown.com/lessons/backpropagation-calculus) · 15 min
- [ ] Stanford CS231n — [Backpropagation, intuitions](https://cs231n.github.io/optimization-2/) — up to "Patterns in backward flow" · 25 min

---

## What you need to know

### Backwards, one layer at a time

Start at the output: softmax with cross-entropy has the simplest gradient there is,
`probs − one_hot(y)`, divided by n. Then each layer does two things with the error that
arrives: multiplies by its **input** to get its weight gradient (`h.T @ dlogits`), and by
its **weights** to pass the error further back (`dlogits @ W2.T`).

### relu is a gate

On the way back, relu lets error through only where it was positive on the way forward.
That mask is the most forgotten line in hand-written backprop.

### Check it

Nudge one weight up by 0.00001, then down, and measure the loss. The difference divided
by 0.00002 is the true slope. Do it for every entry. Your backward pass should agree to
about **1e-11**. A missing `1/n` or relu mask shows up as 0.01 or worse — and training
would still "work", slowly, which is why you check.

---

## Exercises

```bash
pytest week-06/day-3 -v
```

Copy `forward.py` from day 2, then write the four functions in `backprop.py`.

---

## Predict-then-run

Delete the relu mask, run the check, and write down the error before you look. Then put
it back.

---

## Before you close the laptop

Commit, push, fill in the signal log.
