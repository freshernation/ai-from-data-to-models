# Week 2 Milestone — Linear regression from scratch

> `LinearRegressionGD` predicts monthly spend, matches scikit-learn to three decimals,
> and `MATHS_NOTES.md` explains the week's four numbers.

---

## The files

| File | Where it comes from |
|---|---|
| `regression.py` | **copy** from `day-4/` |
| `linreg.py` | new: a class with `fit`, `predict`, `score` |
| `MATHS_NOTES.md` | new |

## `MATHS_NOTES.md`

| Section | What goes in it |
|---|---|
| What a gradient is | In words, and how you checked yours |
| Why the learning rate matters | Your three learning rates on x², and the steps on the shop's data |
| What a 90% alarm is worth | The posterior, and why it is so low |
| Why the slope is not 4.5 | What your fit says per order, and why |

At least 50 words each, with a number.

---

## Check it

```bash
pytest week-02/milestone -v
```

## Friday

You draw a loss curve, and two gradient steps on it.
