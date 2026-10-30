# Day 4 — Look before you model

> **By the end of today** you can save a plot, compute a rate per bucket, and find a
> column that gives away the answer.

---

## Read first

- [ ] Matplotlib — [Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html) — up to "Styling Artists" · 15 min
- [ ] scikit-learn — [Common pitfalls: data leakage](https://scikit-learn.org/stable/common_pitfalls.html) — "Data leakage" section · 10 min

---

## What you need to know

### Save plots; do not show them

`fig.savefig("spend.png")` works on any machine, in tests and on servers. `plt.show()`
opens a window, which tests cannot see. Close the figure after saving.

### Rates by bucket find the signal

`pd.cut` sorts a number into ranges. Customers who ordered in the last 15 days churn at
6.4%; customers silent for 60 days or more churn at **48%**. That one plot tells you more
than a model will until week 3.

### A leak is a column written after the event

`cancel_reason` is filled in only for customers who already left. Group by "is it empty?",
predict the majority in each group, and you are right 100% of the time. An honest column
like `plan` does no better than the baseline on its own. A perfect score from one column
is not a discovery; it is a leak. Find leaks with code, not by reading column names,
because next month's export may leak a different one.

---

## Exercises

```bash
pytest week-01/day-4 -v
```

Write the four functions in `eda.py`. Then save a histogram of `monthly_spend` and look at it.

---

## Predict-then-run

Before running `find_leaks` on the raw export, write down which columns you think it will
return.

---

## Before you close the laptop

Commit, push, fill in the signal log. Then start the milestone.
