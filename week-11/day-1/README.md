# Day 1 — Writing, one word at a time

> **By the end of today** you can build a model that writes reviews, sample from it, and
> say what temperature and top-k change — with numbers.

---

## Read first

- [ ] Dive into Deep Learning — [Language models](https://d2l.ai/chapter_recurrent-neural-networks/language-model.html) — 9.3.1 and 9.3.2 · 15 min
- [ ] Hugging Face — [Generation strategies](https://huggingface.co/docs/transformers/generation_strategies) — "Greedy search" and "Multinomial sampling" · 10 min

---

## What you need to know

### Predict the next word, then roll a die

A language model gives a probability for every possible next word. Generation picks one,
appends it, and asks again. Today's model is the simplest: the chance of each word
given only the one before it, counted from 3,000 reviews. A large language model does
the same thing with a transformer looking at everything so far.

### Temperature and top-k

Divide the log-probabilities by a **temperature** before the softmax: below 1 sharpens
the distribution, above 1 flattens it. **Top-k** keeps only the k likeliest words.
Top-k = 1 is "always take the likeliest" — greedy.

### The finding

| setting | different samples | copied word for word from training |
|---|---|---|
| greedy (top-k 1) | **1 of 200** | 0% |
| temperature 1.0 | 97% | **31%** |
| temperature 1.5 | 99% | 20.5% |

Greedy writes one sentence forever, and it is not a real review: "arrived on time this
shop honestly not very terrible". Sampling is varied — and copies its training data a
third of the time. Both are why real systems sample with care, and why a model can leak
what it was trained on.

---

## Exercises

```bash
pytest week-11/day-1 -v
```

Copy `text.py`, then write the four functions in `generate.py`.

---

## Predict-then-run

Before running the greedy survey: how many different reviews will 200 greedy samples
give? Then explain the one it writes.

---

## Before you close the laptop

Commit, push, fill in the signal log.
