# Day 3 — Probability, and the base rate

> **By the end of today** you can compute a variance, the height of a bell curve and a
> Bayes posterior — and confirm the posterior by simulating 100,000 customers.

---

## Read first

- [ ] 3Blue1Brown — [Bayes theorem](https://www.3blue1brown.com/lessons/bayes-theorem) · 15 min
- [ ] Dive into Deep Learning — [Probability and statistics](https://d2l.ai/chapter_preliminaries/probability.html) — up to "Multiple random variables" · 20 min

---

## What you need to know

### Mean, variance, standard deviation

Variance is the average squared distance from the mean; the standard deviation is its
square root, back in the original units. A **sample** variance divides by n − 1, because
a sample's own mean sits closer to it than the true mean does.

### The normal distribution

The bell curve, set by its mean and standard deviation. Week 2's noise and many measured
quantities look like it. `normal_pdf` gives its height at a point.

### Bayes: what an alarm is worth

An alarm catches 90% of leavers and wrongly flags 10% of stayers. Only 13.05% of the
shop's customers leave. Of everyone the alarm flags, how many actually leave?

`P(leaves | alarm) = 0.9 × 0.1305 / (0.9 × 0.1305 + 0.1 × 0.8695) = 57.5%`

Four alarms in ten are false. The base rate wins: stayers outnumber leavers almost
seven to one, so their 10% swamps the leavers' 90%. Your simulation agrees.

---

## Exercises

```bash
pytest week-02/day-3 -v
```

Write the five functions in `probability.py`.

---

## Predict-then-run

Before computing: if only 1% of customers left, would the alarm's posterior be above or
below 10%?

---

## Before you close the laptop

Commit, push, fill in the signal log.
