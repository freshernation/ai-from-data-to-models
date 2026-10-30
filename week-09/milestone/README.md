# Week 9 Milestone — Sentiment, and every mistake read

> The LSTM sentiment model, an accuracy breakdown by kind of review, and `ERRORS.md`:
> what is left wrong, and whose fault it is.

---

## The files

| File | Where it comes from |
|---|---|
| `text.py` | **copy** from `day-1/` |
| `trainer.py` | **copy** from `week-07/milestone/` |
| `embeddings.py` | **copy** from `day-3/` |
| `lstm.py` | **copy** from `day-4/` |
| `sentiment.py` | new: `train`, `breakdown`, `errors` |
| `ERRORS.md` | new |

## `ERRORS.md`

| Section | What goes in it |
|---|---|
| The numbers | The breakdown, beside week 3's line |
| What the mistakes have in common | After reading every one |
| Which mistakes are the model's fault | And which are the data's |
| What I would do next | For the data, then for the model |

At least 50 words each.

---

## Check it

```bash
pytest week-09/milestone -v
python week-09/milestone/sentiment.py
```

## Friday

The instructor types reviews; you predict both models' answers first.
