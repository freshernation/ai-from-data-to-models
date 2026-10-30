# Week 9 — Friday defence

Forty minutes. It starts with a review the instructor types.

---

## Phase 0 — Live (5 min)

The instructor types three reviews into your trained model: "not good", "not really
good", and one of their own. Before each runs, say what the TF-IDF model would answer,
and what the LSTM will.

## Phase 1 — Explain (10 min)

1. *"The word-count model scores 2.6% on negated reviews — worse than a coin. How?"* — Each negated review contains the opposite adjective; the model trusts the adjective and has no way to attach "not" to it. Best question of the week.
2. *"Why does the averaged-embedding model fail the same way?"* — An average is order-free too; "not" becomes a mildly positive word.
3. *"Word pairs (bigrams) would fix 'not bad'. Why not stop there?"* — They fail on "not really bad"; each n fixes one more word of distance; the LSTM learns any distance.
4. *"Fifteen of your 18 mistakes are mislabelled reviews. So is the model 99.7% accurate?"* — On the labels as they are, 98.2%; on what the text says, about 99.7%; the test labels need fixing before comparing models.
5. *"Why take the LSTM's output at the last real token?"* — After that it only reads padding; the end of the padded row has drifted.

## Phase 2 — Mutate (10 min)

- *"Add a third class, 'neutral'."* — What changes in the model, the loss and the data?
- *"Reviews are now 200 words long."* — What breaks first: memory, speed, or what the LSTM remembers from the start?

## Phase 3 — Debug (10 min)

| Seed | Break | Probes |
|---|---|---|
| Easy | Vocab built from train + test | Works, slightly better — do they see the leak? |
| Medium | `padding_idx` missing in `nn.Embedding` | Padding learns a vector; averages shift with length |
| Medium | LSTM output taken at `[:, -1]` | Long and short reviews behave differently; accuracy drops a few points |
| Nasty | `clean` strips the apostrophe and "isn't" becomes "isn t" | No error; a new class of negation the model never saw; nothing in this data exposes it |

The **Nasty** one: preprocessing decides what the model can see, silently.

---

## Scoring

| Phase | 5 | 3 | 1 |
|---|---|---|---|
| **Live** | Predicts both models' answers correctly before running | One of the two | Guesses |
| **Explain** | Order, distance and label noise in their own words | Needs prompting | Recites |
| **Mutate** | Names every line before typing | Gets there | Cannot place the change |
| **Debug** | Suspects the silent one | Finds it | Guesses |

---

## Instructor: framing week 10

> **The LSTM reads one word at a time and has to carry "not" forward in its memory.**
> Next week every word looks at every other word at once — attention — and you will find
> out what it loses if you forget to tell it where each word sits.
