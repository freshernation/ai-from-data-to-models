# Week 10 — Friday defence

Forty minutes. It starts with a drawing.

---

## Phase 0 — Draw (5 min)

Draw the attention weights for "not really good" as a 3 × 3 grid, before running
anything: where do you expect the weight from "good" to go? Then draw what a
look-only-backwards mask would blank out.

## Phase 1 — Explain (10 min)

1. *"Your transformer without positions scored 98%. So are positions useless?"* — Not in general; in this data the label depends on which words occur together, not their order. A review like "good, not bad" vs "bad, not good" would need them. Best question of the week.
2. *"The LSTM falls to 65% on shuffled reviews and the transformer does not. Which is better?"* — Neither, on this data; they learned different things. The LSTM relies on order; the transformer on co-occurrence. Which matters depends on the reviews you will get.
3. *"Why divide the scores by √d?"* — Dot products grow with dimension; large scores make softmax near one-hot and its gradients tiny.
4. *"How can a model handle a word it never saw?"* — Subwords: 'unbreakable' becomes known pieces; nothing is `<unk>`.
5. *"What does the padding mask do, and what if you forgot it?"* — Stops real words attending to padding; without it a review's answer changes with its padded length.

## Phase 2 — Mutate (10 min)

- *"Two layers instead of one."* — One argument; what happens to the weight count and the training time?
- *"Make the encoder look only backwards."* — Which mask, where — and what kind of model is that the start of?

## Phase 3 — Debug (10 min)

| Seed | Break | Probes |
|---|---|---|
| Easy | `K` not transposed in `attention` | Shape error for non-square inputs |
| Medium | Softmax over the wrong axis | Weights sum to 1 down columns, not across rows; outputs plausible |
| Medium | Position code added after the encoder | Order still invisible; the shuffle test exposes it |
| Nasty | Mean pooling includes the padding positions | No error; short reviews get diluted; accuracy drops a point or two and varies with batch padding |

The **Nasty** one: padding is data unless you say otherwise.

---

## Scoring

| Phase | 5 | 3 | 1 |
|---|---|---|---|
| **Draw** | A sensible grid and the right mask | One of the two | Cannot draw them |
| **Explain** | Order vs co-occurrence, with the shuffle numbers | Needs prompting | "Transformers are better" |
| **Mutate** | Names every line before typing | Gets there | Cannot place the change |
| **Debug** | Suspects the silent one | Finds it | Guesses |

---

## Instructor: framing week 11

> **Mask the encoder to look only backwards and train it to predict the next word, and
> it writes.** Next week: generation, then someone else's very large one behind an API —
> and the honest comparison between it and the models you trained.
