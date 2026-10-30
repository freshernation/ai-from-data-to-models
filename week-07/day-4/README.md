# Day 4 — Is a network worth it here?

> **By the end of today** you can train a churn network with early stopping on a
> validation slice, and decide with numbers whether it beats the line and the forest.

---

## Read first

- [ ] Grinsztajn, Oyallon and Varoquaux — [Why do tree-based models still outperform deep learning on tabular data?](https://arxiv.org/abs/2207.08815) — the abstract and section 5 (open the PDF) · 20 min
- [ ] PyTorch — [Save and load the model](https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html) — "Saving and loading model weights" · 5 min

---

## What you need to know

### A validation slice from the training customers

Hold back 300 of the 1,500 training customers. Standardise with the other 1,200's means.
Choose the best epoch on the 300. The 500 test customers are still untouched.

### One logit

For two classes a network can output one number: the log-odds of leaving.
`BCEWithLogitsLoss` applies the sigmoid itself, safely. Week 3's logistic regression is
exactly this network with no hidden layer.

### The finding

| model | test AUC |
|---|---|
| week 3 line | 0.779 |
| week 4 forest | 0.765 |
| this network, three seeds | 0.784 – 0.787 |

The network is ahead by less than its own seed-to-seed spread, on a test set with 65
leavers. That is a tie, and the line is cheaper, repeatable and explainable. Networks win
when the input is something a line cannot read. Next week it is.

---

## Exercises

```bash
pytest week-07/day-4 -v
```

Write the six functions in `tabular_net.py`.

---

## Predict-then-run

Write down the test AUC you expect before you run it. Then explain the difference in one
line of your signal log.

---

## Before you close the laptop

Commit, push, fill in the signal log. Then start the milestone.
