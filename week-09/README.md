# Week 9 — Text: counts to sequences

> **Destination**
> You can turn reviews into numbers three ways — word counts, learned word vectors and an
> LSTM that reads in order — measure each on the reviews that say "not", and read every
> remaining mistake until you know whose fault it is.

The shop's reviews are the first data where *order* carries the meaning. "Not bad at all"
contains the word "bad". This week starts with week 3's line on word counts, which is
excellent on plain reviews and almost always wrong on negated ones, then moves step by
step to a model that reads left to right. Each step is measured on the same frozen 1,000
reviews, split into plain, "not bad" and "not really bad".

---

## The week

| Day | Folder | What you'll be able to do |
|---|---|---|
| Mon | `day-1/` | Clean, tokenise and encode reviews with a vocabulary |
| Tue | `day-2/` | Build TF-IDF by hand, train a line on it, and measure the negation failure |
| Wed | `day-3/` | Learn word vectors with `nn.Embedding`, and see what averaging cannot know |
| Thu | `day-4/` | Read reviews in order with an LSTM |
| Fri | `milestone/` | The sentiment model, its breakdown, and `ERRORS.md` |

---

## The rule from this week on

**Report the score on the cases that matter, not only the average.** 65% overall hides
98.6% on plain reviews and 2.6% on negated ones.

---

## Before Monday

Nothing new to install. The reviews are in `data/reviews.csv`; `shoplab.reviews` loads them.

---

## Outside-view question

> *A translator meets "not bad at all". What do they keep from the word order that a list
> of the words would lose — and what do they do when the order is unusual?*
