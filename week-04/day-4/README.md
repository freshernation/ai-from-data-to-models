# Day 4 — Better inputs, and what the model leans on

> **By the end of today** you can add engineered features, measure whether they helped,
> and rank columns by how much the model needs them.

---

## Read first

- [ ] scikit-learn — [Permutation feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html) — the outline of the algorithm, and "Misleading values on strongly correlated features" · 15 min
- [ ] Mitchell et al. — [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993) — the abstract and section 4 (open the PDF) · 15 min

---

## What you need to know

### Feature engineering

A feature is a column you compute: spend per order, a flag for the basic plan, a flag
for 60 days of silence. It helps when it hands the model something it cannot build
itself. A line cannot say "basic plan"; a tree can already split on "60 days".

### Permutation importance

Shuffle one column in the test set and score again. The drop is how much the model
needed that column. No column is removed and nothing is retrained.

### The finding

Shuffle days since the last order and boosting's AUC falls by **0.139** — more than all
the other columns together. Your `silent_60` flag scores **0.0**: the trees already split
on the raw column. The four features move the line from **0.779** to **0.780**. Features
are cheap to add; evidence that they help is not.

---

## Exercises

```bash
pytest week-04/day-4 -v
```

Write `add_features` and `permutation_importance` in `features.py`.

---

## Predict-then-run

Rank the six raw columns by importance before you run it.

---

## Before you close the laptop

Commit, push, fill in the signal log. Then start Project 1.
