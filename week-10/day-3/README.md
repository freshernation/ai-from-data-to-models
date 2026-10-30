# Day 3 — A tiny transformer

> **By the end of today** you can build a transformer encoder classifier in PyTorch,
> train it on the reviews, and explain why it scores the same with or without positions.

---

## Read first

- [ ] PyTorch — [`nn.TransformerEncoderLayer`](https://docs.pytorch.org/docs/stable/generated/torch.nn.TransformerEncoderLayer.html) — the description and the `batch_first` argument · 10 min
- [ ] Dive into Deep Learning — [The transformer architecture](https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html) — 11.7.1 and 11.7.4 · 20 min

---

## What you need to know

### The block

Embedding (scaled by √dim) plus position → one encoder layer (attention, then a small
feed-forward network, each with a residual connection and layer normalisation) → the
mean over real words → a line to two classes. **10,306 weights**, eight seconds of training.

### The padding mask

`src_key_padding_mask` is Monday's mask: padding is never attended to. Then average only
the real positions. Get either wrong and a review's answer changes with how long the
other reviews in its batch are.

### The finding

With positions: about **98%**. Without: also about **98%**. In these reviews the label is
decided by *which* words appear together — "not" with "bad" — never by their order. The
TF-IDF line failed because it could only *add* words; attention *combines* them, even
blind to order. Tomorrow's milestone asks the same question of the LSTM.

---

## Exercises

```bash
pytest week-10/day-3 -v
```

Copy `text.py`, `trainer.py` and `embeddings.py`, then write `transformer.py`. Train with
`lr=0.005`.

---

## Predict-then-run

Before training without positions, write down the accuracy you expect, and why.

---

## Before you close the laptop

Commit, push, fill in the signal log.
