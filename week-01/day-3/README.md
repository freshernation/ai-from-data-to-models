# Day 3 — Cleaning, and counting what you cleaned

> **By the end of today** you can remove duplicates, unify spellings, turn impossible
> values into missing ones, fill gaps sensibly — and report how many of each you fixed.

---

## Read first

- [ ] pandas — [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) — up to "Filling missing data" · 20 min
- [ ] pandas — [Working with text data](https://pandas.pydata.org/docs/user_guide/text.html) — "String methods" only · 10 min

---

## What you need to know

### A fix you cannot count is a fix you cannot report

Each function returns the cleaned frame *and* a number. The data report on Friday quotes
those numbers; the manager wants "37 duplicates", not "some duplicates".

### Missing is not zero

A spend of -1.0 is impossible. Setting it to 0 invents a customer who spends nothing.
Setting it to NaN says "unknown", and unknown gets filled with something defensible: the
median spend of customers on the same plan. The median, because a few big spenders drag
the mean.

### Order matters

Fix impossible values *before* filling, or the -1s are never filled. The export has 37
duplicates, 12 spellings of 4 regions, 12 impossible spends and 60 gaps — 72 values to fill.

### Never change the caller's frame

`df.copy()` first. A cleaning function that edits its input in place makes every test
after it see different data.

---

## Exercises

```bash
pytest week-01/day-3 -v
```

Write the five functions in `clean.py`.

---

## Predict-then-run

Before running: if you filled the gaps with the overall mean instead of each plan's
median, would pro customers' filled spends go up or down?

---

## Before you close the laptop

Commit, push, fill in the signal log.
