# Week 2 — The maths, in code

> **Destination**
> You can compute a gradient two ways and show they agree, pick a learning rate that
> converges, say what a "90% accurate" alarm is worth at the shop's base rate, and fit a
> line from scratch that matches scikit-learn's to three decimal places.

Next week a model learns a churn threshold for you. To trust it, you need the three ideas
it rests on: a model is a weighted sum (matrices), learning is walking downhill
(gradients), and its output is a probability (Bayes). Each one is code you can test, not
notation you memorise. No proofs this week; every formula is checked against a number.

---

## The week

| Day | Folder | What you'll be able to do |
|---|---|---|
| Mon | `day-1/` | Multiply matrices by hand, then write a linear model as `X @ w + b` |
| Tue | `day-2/` | Check a gradient by finite differences and watch a learning rate diverge |
| Wed | `day-3/` | Compute a variance and a Bayes posterior, and confirm both by simulation |
| Thu | `day-4/` | Fit a line exactly and by gradient descent, and see what scaling buys |
| Fri | `milestone/` | `LinearRegressionGD`, matching scikit-learn, and `MATHS_NOTES.md` |

---

## The rule from this week on

**Check every formula against a number you can compute another way.** An analytic
gradient is checked by finite differences, a probability by simulation, a fit by the
library's.

---

## Before Monday

Nothing new to install. If algebra is your weak area in `logs/baseline.md`, do the
Monday reading twice.

---

## Outside-view question

> *A surveyor measures a field with a tape. How do they know the tape is right?*
