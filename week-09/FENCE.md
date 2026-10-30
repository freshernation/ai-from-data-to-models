# Week 9 — Concept fence

## Allowed

**Everything from weeks 1 to 8**, plus:

- `re`, `collections.Counter`; tokenising, vocabularies, padding
- bag of words and TF-IDF by hand; scikit-learn's `TfidfVectorizer` only in tests
- `nn.Embedding`, `nn.LSTM`; picking the output at each sequence's last real token

## Not yet

attention and transformers (week 10) · subword tokenisers (week 10) · pretrained word vectors
(word2vec, GloVe files) · `pack_padded_sequence` · bidirectional and stacked LSTMs · spaCy, NLTK

---

## Why no stemming or stop-word lists

The poster's syllabus lists them, and older tutorials start there. Removing "stop words"
would delete "not", the most important word in this week's data. Stemming merges words a
model can learn to treat alike anyway. Both are choices a model trained end to end makes
better than a list typed by hand, and both hide the week's finding.
