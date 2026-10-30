# Week 7 Milestone — One loop, every model

> `trainer.fit`, the training loop with early stopping that weeks 8 to 10 reuse, a churn
> network trained by it, and `COMPARISON.md` choosing one churn model to keep.

---

## The files

| File | Where it comes from |
|---|---|
| `trainer.py` | new: `fit()` with validation, early stopping and the best state restored |
| `churn_net.py` | new: the churn network trained by `fit()` |
| `COMPARISON.md` | new |

## `COMPARISON.md`

| Section | What goes in it |
|---|---|
| The candidates | Every churn model from weeks 3, 4 and 7 |
| The numbers | Their test AUCs, side by side |
| How much of the difference is noise | Seeds, and 65 leavers |
| What I would ship, and why | One model, defended |

At least 50 words each.

---

## Check it

```bash
pytest week-07/milestone -v
python week-07/milestone/churn_net.py
```

## Friday

You sketch the loss curves before anyone shows you a plot.
