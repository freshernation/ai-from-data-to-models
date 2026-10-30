# Week 1 Milestone — A file a model can train on

> `prepare.py` turns the raw export into a clean file, and `DATA_REPORT.md` tells the
> shop manager what was wrong with it.

---

## The files

| File | Where it comes from |
|---|---|
| `clean.py` | **copy** from `day-3/` |
| `eda.py` | **copy** from `day-4/` |
| `prepare.py` | new: clean, find leaks, drop them, write the CSV |
| `DATA_REPORT.md` | new |

## `DATA_REPORT.md`

| Section | What goes in it |
|---|---|
| The data | Rows, columns, customers, the churn rate and the baseline it implies |
| What was wrong | Each fault and its count, from `prepare()`'s report |
| The leak | Which column, how you found it, why it must go |
| What I would ask the data owner | Questions only they can answer |

At least 40 words a section, and your own numbers.

---

## Check it

```bash
pytest week-01/milestone -v
python week-01/milestone/prepare.py
```

## Friday

You clone your repo fresh, run `prepare.py`, and read your report aloud.
