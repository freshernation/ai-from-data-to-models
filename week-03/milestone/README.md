# Week 3 Milestone — Churn v1

> A churn model trained on the frozen training set, thresholded on costs, scored once on
> the frozen test set, and `EVAL.md` explaining every number to the shop manager.

---

## The files

| File | Where it comes from |
|---|---|
| `logistic.py` | **copy** from `day-2/` |
| `metrics.py` | **copy** from `day-3/` |
| `thresholds.py` | **copy** from `day-4/` |
| `churn_v1.py` | new: `train()` and `evaluate()` |
| `EVAL.md` | new |

## `EVAL.md`

| Section | What goes in it |
|---|---|
| What the model does | Inputs, output, who gets an offer |
| How it was tested | The split, and what was chosen on which data |
| The numbers, beside the baseline | Accuracy, baseline, recall, precision, AUC |
| Why the threshold is not 0.5 | The costs, and the value at both thresholds |
| What would make me distrust it | Assumptions, and how much noise 65 leavers allows |

At least 50 words each.

---

## Check it

```bash
pytest week-03/milestone -v
python week-03/milestone/churn_v1.py
```

## Friday

You run `churn_v1.py` live and read the numbers aloud.
