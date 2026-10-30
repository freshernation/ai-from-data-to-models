# Week 10 — Attention and transformers

> **Destination**
> You can compute attention by hand and match PyTorch, show that without positions it
> cannot tell a sentence from its reverse, train a tiny transformer on the shop's reviews,
> split unseen words into subwords, and say — with a shuffle test — what each of three
> text models actually learned.

Every large language model is a stack of the block you build this week. The LSTM read
one word at a time and carried "not" forward in its memory. Attention lets every word
look at every other word directly. This week you write it by hand, find the one thing it
cannot see without help, and then run an experiment that shows what last week's LSTM
really learned.

---

## The week

| Day | Folder | What you'll be able to do |
|---|---|---|
| Mon | `day-1/` | Compute scaled dot-product attention, with a mask, in numpy |
| Tue | `day-2/` | Show attention is blind to order, and fix it with a position code |
| Wed | `day-3/` | Train a 10,000-weight transformer encoder on the reviews |
| Thu | `day-4/` | Learn byte-pair merges, and run a real pretrained transformer live |
| Fri | `milestone/` | Line vs LSTM vs transformer on one frozen test set, plus a shuffle test, and `RESULTS.md` |

---

## The rule from this week on

**Test what the model relies on, not only how often it is right.** Two models with the
same accuracy can have learned different things; a changed input — shuffled, moved,
darkened — shows which.

---

## Before Monday

Nothing new to install. Optional, for Thursday's live demo only: `pip install transformers`.

---

## Outside-view question

> *A conductor hears one wrong note among a hundred players. How do they find it — by
> listening to each player in turn, or to all of them at once?*
