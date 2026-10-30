# Day 4 — Reading in order

> **By the end of today** you can run an LSTM over a review word by word, take its answer
> at the right position, and show that order fixes negation.

---

## Read first

- [ ] Christopher Olah — [Understanding LSTM networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) — up to "Variants on LSTMs" · 25 min
- [ ] PyTorch — [`nn.LSTM`](https://docs.pytorch.org/docs/stable/generated/torch.nn.LSTM.html) — "Inputs" and "Outputs", with `batch_first=True` · 10 min

---

## What you need to know

### A loop with a memory

An LSTM reads one word vector at a time and updates a hidden state: what it has read so
far. After "not", the state can carry "flip the next adjective". It is a network applied
in a loop, with gates that decide what to keep.

### The last real token

`nn.LSTM` returns an output at every position, including the padding. The answer is the
output at each review's **last real word**: count the non-zero ids, subtract one, and pick
that position per row.

### The finding

| | all reviews | negated reviews |
|---|---|---|
| TF-IDF line | 65% | 2.6% |
| averaged embeddings | ~65% | fails the same way |
| LSTM | **~98%** | **~98%**, and ~97% on "not really bad" |

Order was the missing piece. Pairs of words would have fixed "not bad" and failed "not
really bad"; the LSTM handles any distance it has seen.

---

## Exercises

```bash
pytest week-09/day-4 -v
```

Copy `text.py`, `trainer.py` and `embeddings.py`, then write `LSTMClassifier` in `lstm.py`.

---

## Predict-then-run

What happens to accuracy if you take the output at the last *column* instead of the last
real word? Predict, try, put it back.

---

## Before you close the laptop

Commit, push, fill in the signal log. Then start the milestone.
