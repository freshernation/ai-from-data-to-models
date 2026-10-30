# Day 3 — Cross-validation, and the leak inside it

> **By the end of today** you can compare models on training data alone, tune settings
> with a grid, and explain how 500 columns of noise scored AUC 0.74.

---

## Read first

- [ ] scikit-learn — [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) — the introduction and "Stratified k-fold" · 15 min
- [ ] scikit-learn — [Tuning hyper-parameters](https://scikit-learn.org/stable/modules/grid_search.html) — "Exhaustive Grid Search" · 10 min
- [ ] scikit-learn — [Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) — "How to avoid data leakage" · 10 min

---

## What you need to know

### Five small test sets inside the training set

Cut the training customers into five folds. Train on four, score the fifth; rotate. The
mean is your estimate, the spread is how much to trust it. The real test set stays shut.

### A pipeline is one model

`make_pipeline(StandardScaler(), LogisticRegression())` behaves like one model, so each
fold fits its own scaler on its own training part. Anything fitted outside the pipeline —
a scaler, a column selection — has seen every fold's rows.

### The finding

Take 300 rows of 500 columns of pure noise and a coin-flip label. Choose the 20 "best"
columns using all the rows, then cross-validate: AUC **0.74**. A signal, invented. Put the
selection inside the pipeline: **0.47** — a coin. Cross-validation only protects the
steps that are inside it.

### Tuning

`GridSearchCV` tries every combination of settings with cross-validation and keeps the
best. For the forest: `max_features="sqrt"`, `min_samples_leaf=20`, CV AUC 0.811. A
default, untuned SVM scores 0.691. Settings matter; so does testing them honestly.

---

## Exercises

```bash
pytest week-04/day-3 -v
```

Write the six functions in `tuning.py`. `leaky_selection_auc` is wrong on purpose.

---

## Predict-then-run

Before running the noise test, write down what AUC you expect from pure noise. Then
explain the gap in one sentence in your signal log.

---

## Before you close the laptop

Commit, push, fill in the signal log.
