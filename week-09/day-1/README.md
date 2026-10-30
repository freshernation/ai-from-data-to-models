# Day 1 — From a review to numbers

> **By the end of today** you can clean a review, split it into words, build a
> vocabulary and turn any review into a padded row of ids.

---

## Read first

- [ ] Dive into Deep Learning — [Converting raw text into sequence data](https://d2l.ai/chapter_recurrent-neural-networks/text-sequence.html) — 9.2.1 to 9.2.3 · 15 min
- [ ] scikit-learn — [Text feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) — "The Bag of Words representation" · 10 min

---

## What you need to know

### Clean, then split

Lower-case everything, turn punctuation into spaces, split on spaces. "Not BAD!! at
all." becomes `["not", "bad", "at", "all"]`. Keep apostrophes: "isn't" is one word.

### A vocabulary is a numbering

Every word gets an id, most frequent first. Two ids are reserved: 0 for padding, 1 for
"a word I never saw in training". The shop's 3,000 training reviews use only **51**
distinct words, and **"not" is the third most common** — a model that ignores it ignores
a lot.

### Padding

A batch is a rectangle, but reviews have different lengths. Pad short ones with 0 up to
the longest. Tomorrow's model ignores order and padding; Thursday's must handle both.

---

## Exercises

```bash
pytest week-09/day-1 -v
```

Write the five functions in `text.py`.

---

## Predict-then-run

Which word will be the most common in the training reviews? Guess before building the vocabulary.

---

## Before you close the laptop

Commit, push, fill in the signal log.
