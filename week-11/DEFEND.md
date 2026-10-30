# Week 11 — Friday defence

Forty minutes. It starts with an attack the instructor writes.

---

## Phase 0 — Live (5 min)

The instructor writes a new attack review on the spot. Run it through your drafter.
Does the guardrail catch it? If it does not, say which rule you would add — without
blocking the 200 ordinary reviews.

## Phase 1 — Explain (10 min)

1. *"Your guardrail blocked all eight attacks. Is the drafter safe?"* — Safe against those eight, and the guardrail is a word list; "half price next time" passes. Safety is the attacks you tested plus a person in the loop. Best question of the week.
2. *"Why does your own model decide the sentiment, not the LLM?"* — It is 98% accurate, costs nothing per review, and cannot be talked out of its answer by the review.
3. *"Turn 10 of a chat sent 424 tokens; turn 1 sent 25. Why?"* — The model remembers nothing; the whole history is sent and paid for every turn.
4. *"What does temperature do, and why not always use 0?"* — Divides the logits; low makes the likeliest word near certain, which repeats one sentence; high makes odd ones.
5. *"One retry fixed every malformed answer. What did it cost?"* — 19% more calls; and the API offers structured outputs that make the format guaranteed.

## Phase 2 — Mutate (10 min)

- *"Replies must also never mention a competitor."* — Which rule, and what is the false-positive risk?
- *"Switch the drafter to the cheapest model."* — Where does that change, and which number should you re-measure first?

## Phase 3 — Debug (10 min)

| Seed | Break | Probes |
|---|---|---|
| Easy | `cost` uses input price for output tokens | Numbers too low; checked against the hand example? |
| Medium | `classify` retries without sending the bad answer back | Retries return the same mistake |
| Medium | `Chat` appends only the user turns to history | The model "forgets" what it said |
| Nasty | `draft` returns the draft when blocked, and the fallback when clean | No error; every attack reply goes out; `unsafe_sent` catches it — if they kept that check |

The **Nasty** one: a guardrail with its branches swapped passes every "blocked" count.
Measure what actually went out, not what you meant to block.

---

## Scoring

| Phase | 5 | 3 | 1 |
|---|---|---|---|
| **Live** | Predicts the outcome and proposes a rule with its false-positive cost | Runs it | Cannot run it |
| **Explain** | Trust boundaries and cost, in their own words | Needs prompting | "The guardrail makes it safe" |
| **Mutate** | Names every line before typing | Gets there | Cannot place the change |
| **Debug** | Suspects the silent one | Finds it | Guesses |

---

## Instructor: framing week 12

> **Five models, five folders, and nobody can use any of them.** Next week they go
> behind one API, in one container, with a check that tells you when next month's
> customers no longer look like the ones you trained on. Then you defend it.
