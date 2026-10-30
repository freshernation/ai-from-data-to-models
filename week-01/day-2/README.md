# Day 2 — Asking a table questions

> **By the end of today** you can load a CSV with pandas and answer "how many",
> "what fraction" and "which group most" in one line each.

---

## Read first

- [ ] pandas — [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) — "Object creation" to "Grouping" · 25 min
- [ ] pandas — [Group by: split-apply-combine](https://pandas.pydata.org/docs/user_guide/groupby.html) — the first two sections · 10 min

---

## What you need to know

### A DataFrame is columns of arrays with names

```python
df = pd.read_csv("data/customers_raw.csv")
df["churned"].mean()                     # a column is a Series: yesterday's array, with labels
df[df["plan"] == "pro"]                  # rows where the condition holds
df.groupby("plan")["churned"].mean()     # one rate per plan
```

### Group, then aggregate

`groupby` splits the rows by a column's values, applies something to each group, and
glues the answers together. Basic customers churn at about 17%, pro customers at under 5%.

### Today's numbers are slightly wrong, on purpose

You are working on the raw export. Its churn rate is 13.21%; the true one is 13.05%,
because 37 customers appear twice. And a filter for `region == "north"` finds 151
customers, out of 618 who live in the north. Nothing errors. Tomorrow you fix both.

---

## Exercises

```bash
pytest week-01/day-2 -v
```

Write the five functions in `explore.py`.

---

## Predict-then-run

Run `df["region"].unique()` before you write `count_where`. How many regions does the shop have?
How many does pandas think it has?

---

## Before you close the laptop

Commit, push, fill in the signal log.
