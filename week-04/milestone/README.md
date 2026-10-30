# Week 4 Milestone — Project 1: the churn model

> A churn model chosen by cross-validation on training data, saved to a file, scored once
> on the test set, and a model card for whoever decides to use it.

---

## The files

| File | Where it comes from |
|---|---|
| `tuning.py` | **copy** from `day-3/` |
| `features.py` | **copy** from `day-4/` |
| `churn_model.py` | new: candidates, choose, train, predict, save, load |
| `MODEL_CARD.md` | new |

## `MODEL_CARD.md`

| Section | What goes in it |
|---|---|
| Intended use | What it is for, and what it must not be used for |
| Data | Where it came from, its size, its columns |
| How the model was chosen | Each candidate's CV AUC, and the choice |
| Performance | The test AUC, beside a baseline and week 3 |
| What drives it | Permutation importance, and what it does not prove |
| Limits and risks | What would make it wrong |

At least 50 words each.

---

## Check it

```bash
pytest week-04/milestone -v
python week-04/milestone/churn_model.py
```

## Friday

You run it, then load the saved model in a fresh session and score a customer the
instructor invents.
