# Week 6 — Friday defence

Forty minutes. It starts at the whiteboard.

---

## Phase 0 — Draw (5 min)

Draw the network with every shape: X (450, 2) → W1 → h → W2 → probs. Then draw the
backward pass: which arrays are multiplied to get dW1?

## Phase 1 — Explain (10 min)

1. *"Why can't a perceptron learn XOR?"* — No straight line separates the two classes; the four corners alternate.
2. *"Your weights all start at zero. What happens and why?"* — Every hidden unit outputs zero, relu passes no gradient, nothing updates; the loss stays at ln 2. Best question of the week.
3. *"What does the finite-difference check prove, and what does it not?"* — That backward matches the loss you wrote; not that the loss is the right one.
4. *"Why subtract the row max in softmax?"* — exp overflows for large logits; the shift cancels in the ratio.
5. *"The network beats the line by 3.3 points on moons. Is that worth a hidden layer?"* — Measured gain small because the moons are mostly linearly separable; on XOR it is the difference between 50% and 100%.

## Phase 2 — Mutate (10 min)

- *"Use sigmoid instead of relu in the hidden layer."* — Which two lines in forward and backward change?
- *"Three classes instead of two."* — What changes? (Nothing in the code — why not?)

## Phase 3 — Debug (10 min)

| Seed | Break | Probes |
|---|---|---|
| Easy | `W2.T` written `W2` in backward | Shape error — they read the shapes |
| Medium | Missing `/ n` in dlogits | Gradient check fails by a factor of n; training still works with a smaller lr |
| Medium | Loss recorded after the update | Off-by-one in the curve; does any test notice? |
| Nasty | `backward` edits `cache["probs"]` in place (no `.copy()`) | No error, gradients right, training fine — but an accuracy computed from the cache afterwards reads probabilities with 1 subtracted |

The **Nasty** one: numpy arrays are shared, not copied. Editing one in place changes it
for everyone holding it, and nothing complains.

---

## Scoring

| Phase | 5 | 3 | 1 |
|---|---|---|---|
| **Draw** | Every shape, forward and back | Forward only | Cannot draw it |
| **Explain** | Zero-init and the check in their own words | Needs prompting | Recites |
| **Mutate** | Names every line before typing | Gets there | Cannot place the change |
| **Debug** | Suspects the silent one | Finds it | Guesses |

---

## Instructor: framing week 7

> **Next week the forty lines you wrote on Wednesday become `.backward()`.** Then the
> network gets bigger than its data, and you learn the three ways to stop it memorising —
> and find out whether any of it beats week 4 on the shop's own customers.
