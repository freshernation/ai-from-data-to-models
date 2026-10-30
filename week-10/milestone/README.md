# Week 10 Milestone — Three ways to read a review

> The TF-IDF line, the LSTM and your transformer on the same frozen test set, with a
> shuffle test that shows what each relies on, and `RESULTS.md`.

---

## The files

| File | Where it comes from |
|---|---|
| `text.py`, `trainer.py`, `embeddings.py`, `lstm.py`, `bow.py` | **copy** from week 9 (and week 7's `trainer.py`) |
| `transformer.py` | **copy** from `day-3/` |
| `compare.py` | new: `shuffled`, `row`, `compare` |
| `RESULTS.md` | new |

## `RESULTS.md`

| Section | What goes in it |
|---|---|
| The table | Every number from `compare.py` |
| What each model can and cannot see | In plain words |
| The shuffle test | What it shows about each model |
| What I would use, and when I would change my mind | One choice, and its conditions |

At least 50 words each.

---

## Check it

```bash
pytest week-10/milestone -v
python week-10/milestone/compare.py
```

## Friday

You draw the attention grid for "not really good" before anything runs.
