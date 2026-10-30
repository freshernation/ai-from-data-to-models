# Week 4 — Trees, ensembles and tuning (Project 1)

> **Destination**
> You can build a decision tree's first split by hand, show a deep tree memorising, choose
> between a line, a forest and boosting by cross-validation without opening the test set,
> catch a leak that hides inside cross-validation, and ship a saved churn model with a model card.

Trees and their ensembles are the strongest models there are for tables like the shop's
— in general. This week you build one question by hand, then let hundreds of trees vote,
then find out that on *this* table they do not beat week 3's line. That is not a failure:
it is the week's most useful result, because you find it out by cross-validation on
training data, before the test set is ever opened.

---

## The week

| Day | Folder | What you'll be able to do |
|---|---|---|
| Mon | `day-1/` | Compute Gini impurity and find the best split by hand |
| Tue | `day-2/` | Show a deep tree memorising, and score a forest and boosting |
| Wed | `day-3/` | Cross-validate, tune with a grid, and catch selection leaking into the folds |
| Thu | `day-4/` | Engineer features and measure which ones the model leans on |
| Fri | `milestone/` | **Project 1**: the chosen, saved churn model, and `MODEL_CARD.md` |

---

## The rule from this week on

**Every choice is made inside cross-validation on training data** — model, settings,
features, columns. A step that looks at all the data before the folds are cut leaks.

---

## Before Monday

Nothing new to install: `joblib` comes with scikit-learn.

---

## Outside-view question

> *A bank's loan officer must be able to explain every refusal. What are they never
> allowed to say, and why?*
