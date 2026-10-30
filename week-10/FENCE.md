# Week 10 — Concept fence

## Allowed

**Everything from weeks 1 to 9**, plus:

- scaled dot-product attention and masks by hand; sinusoidal position codes
- `nn.TransformerEncoderLayer`, `nn.TransformerEncoder`, `register_buffer`
- `F.scaled_dot_product_attention` — only in tests, to check yours
- byte-pair encoding by hand; `transformers` — **only** in the given `pretrained_live.py`

## Not yet

generating text (week 11) · decoder-only models and causal language modelling (week 11) ·
fine-tuning a pretrained model (the `fine-tuning` course) · multi-head attention by hand ·
learned position embeddings · the `tokenizers` library

---

## Why not fine-tune BERT on the reviews

It would score about as well, after a 260 MB download and minutes of training per run,
and nothing in the result would be yours to explain. A 10,000-weight transformer you
wrote reaches the same ceiling in eight seconds, and every part of it is something you
built this week. Thursday runs a real pretrained model live, so you see what one is; the
`fine-tuning` course is where you adapt one.
