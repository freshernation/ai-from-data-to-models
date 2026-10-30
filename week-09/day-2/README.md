# Day 2 — Counting words, and what counting cannot see

> **By the end of today** you can build TF-IDF by hand, match scikit-learn, train week 3's
> line on it, and show exactly where it fails.

---

## Read first

- [ ] scikit-learn — [Tf–idf term weighting](https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting) · 15 min
- [ ] Jurafsky and Martin — [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) — chapter 4, section 4.4 "Optimizing for sentiment analysis" (open the PDF) · 10 min

---

## What you need to know

### Bag of words

One column per word, one row per review, the count in the cell. Order is gone: "not bad,
good" and "bad, not good" are the same row.

### TF-IDF

Weight each count by how rare the word is across reviews (`ln((1 + n) / (1 + df)) + 1`),
then scale each row to length 1. Common words like "the" count for less.

### The finding

| reviews | accuracy |
|---|---|
| plain ("the mug is lovely") | **98.6%** |
| negated ("not bad at all") | **2.6%** |
| all | 65.0% |

Worse than a coin on negated reviews, because every negated review contains the
*opposite* adjective, and the model trusts the adjective. "Not" has one weight, and it
cannot attach to the word after it.

---

## Exercises

```bash
pytest week-09/day-2 -v
```

Copy `text.py`, then write the seven functions in `bow.py`.

---

## Predict-then-run

Add word *pairs* as features (`TfidfVectorizer(ngram_range=(1, 2))`, in a scratch file).
Predict the accuracy on "not bad" — and on "not really bad". Then run it. (About 99% and 24%.)

---

## Before you close the laptop

Commit, push, fill in the signal log.
