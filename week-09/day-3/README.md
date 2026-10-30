# Day 3 — Words as vectors

> **By the end of today** you can learn a vector for every word with `nn.Embedding`, show
> that the model discovered which words are positive, and explain why it still fails on "not".

---

## Read first

- [ ] PyTorch — [`nn.Embedding`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Embedding.html) — the description and `padding_idx` · 5 min
- [ ] Dive into Deep Learning — [Word embedding (word2vec)](https://d2l.ai/chapter_natural-language-processing-pretraining/word2vec.html) — 15.1.1 and 15.1.2 · 15 min

---

## What you need to know

### An embedding is a lookup table that learns

`nn.Embedding(53, 16)` holds a 16-number vector for each word id. Training moves the
vectors so the model's answers improve. Similar words drift together — week 5's cosine
similarity, now on learned vectors.

### Averaging

Average the vectors of a review's real words (not the padding) and put a line on top.
It is the word-count model again, with learned features instead of counts — and still
blind to order.

### The finding

Nobody told the model which words are positive. Along its own positive-minus-negative
direction, **every** positive adjective scores above zero and **every** negative one below.
And **"not" scores mildly positive**: it appears mostly in "not bad", "not awful". An
average cannot know what "not" is next to, so accuracy stays near **65%**.

---

## Exercises

```bash
pytest week-09/day-3 -v
```

Copy `text.py` and your week 7 `trainer.py`, then write `embeddings.py`.

---

## Predict-then-run

Before running `nearest(model, vocab, "great")`: which five words do you expect? Then
explain any surprises — some words barely move from where they started.

---

## Before you close the laptop

Commit, push, fill in the signal log.
