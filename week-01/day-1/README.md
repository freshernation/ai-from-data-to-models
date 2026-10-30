# Day 1 — A rule, a baseline, and an array

> **By the end of today** you can turn a manager's rule into code, score it, and say
> whether it beats predicting "nobody leaves" — without writing a loop.

---

## Read first

- [ ] NumPy — [the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) — up to "Basic array operations" · 25 min
- [ ] Google — [ML Crash Course: framing](https://developers.google.com/machine-learning/crash-course) — the introduction only · 10 min

---

## What you need to know

### What "AI" means in this course

A program you write by hand follows rules you chose. A **model** follows rules it
*learned* from examples. Everything people call AI today — from a spam filter to a chat
assistant — is the second kind. This course builds the second kind, from the simplest
(a line, in week 2) to a transformer (week 10). Today you write the first kind, so that
you have something to beat.

### An array is a whole column at once

```python
import numpy as np
tickets = np.array([0, 3, 1, 5])
tickets >= 3                    # array([False,  True, False,  True])
(tickets >= 3).astype(int)      # array([0, 1, 0, 1])
(tickets >= 3).mean()           # 0.5  <- True counts as 1
```

A comparison gives an array of True/False; `.mean()` of that is a fraction. That is
accuracy in one line: `(y_true == y_pred).mean()`.

### The baseline

Before judging any prediction, ask what the dumbest one scores. Here, 13.05% of
customers leave, so predicting "nobody leaves" is right 86.95% of the time.

The manager's rule — three or more tickets means leaving — is right **85.5%** of the
time. It sounds sensible, it catches 26 real leavers, and it scores *lower than doing
nothing*. Try every threshold from 0 to 10 and none of them beats the baseline. Accuracy
alone hides what the rule is doing; week 3 gives you measures that do not.

---

## Exercises

```bash
pytest week-01/day-1 -v
```

Write the four functions in `first_rule.py`. `shoplab.customers.arrays(["support_tickets", "churned"])`
gives you the two columns as arrays if you want to try them by hand.

---

## Predict-then-run

Before running the finding test, write down: what accuracy does "three or more tickets"
get? Higher or lower than 86.95%?

---

## Before you close the laptop

Commit, push, fill in the signal log.
