# Day 4 — Subwords, and a transformer someone else trained

> **By the end of today** you can learn byte-pair merges from the reviews, split a word
> nobody has seen into known pieces, and run a real pretrained transformer on the shop's text.

---

## Read first

- [ ] Hugging Face — [Byte-pair encoding tokenization](https://huggingface.co/learn/llm-course/chapter6/5) — up to "Implementing BPE" · 15 min
- [ ] Sennrich, Haddow and Birch — [Neural machine translation of rare words with subword units](https://arxiv.org/abs/1508.07909) — the abstract and section 3.2 (open the PDF) · 10 min

---

## What you need to know

### Merge the most common pair, again and again

Start with characters plus an end marker. Count adjacent pairs across all words, merge
the most frequent into one symbol, repeat. The list of merges *is* the tokenizer.

### The trade

| merges | symbols per word | distinct symbols |
|---|---|---|
| 0 | 5.38 | 25 |
| 60 | 2.43 | 67 |
| 200 | 1.00 | 51 (every word is one token) |

More merges, shorter sequences, bigger vocabulary. Real models choose tens of thousands.

### No unknown words

"unbreakable" never appears in a review, yet with 60 merges it becomes `u n b rea k a
ble_` — pieces the model has seen. That is why every large language model uses subwords.

### Pretrained (live)

`pretrained_live.py` runs DistilBERT, fine-tuned by others on film reviews, on twenty
shop reviews and three hard negations. It needs `pip install transformers` and a 260 MB
download, so no test runs it.

---

## Exercises

```bash
pytest week-10/day-4 -v
```

Copy `text.py`, then write the five functions in `bpe.py`.

---

## Predict-then-run

After 10 merges on the reviews, what will the first merge be? Guess from the most common
word endings.

---

## Before you close the laptop

Commit, push, fill in the signal log. Then start the milestone.
