# Week 2 — Friday defence

Forty minutes. It starts at the whiteboard.

---

## Phase 0 — Draw (5 min)

Draw the loss of a one-weight model as a curve. Mark one gradient step with a small
learning rate, then one with a learning rate that is too big. No code.

## Phase 1 — Explain (10 min)

1. *"How do you know your gradient formula is right?"* — The finite difference agrees to six decimals.
2. *"The data was built with 4.5 per order. Your model says 5.7. Which is wrong?"* — Neither: pro customers order more and spend more; with plan left out, orders absorb it. A coefficient is not a cause. Best question of the week.
3. *"Why does standardising make it converge in 52 steps instead of 58,384?"* — One learning rate must suit every weight; unscaled, tenure's large values force a tiny rate, so orders' weight barely moves.
4. *"A 90% accurate alarm, and 42% of its alarms are false. How?"* — Base rate: stayers outnumber leavers about seven to one.
5. *"Why divide by n - 1 for a sample?"* — The sample mean sits closer to the sample than the true mean does, so n underestimates the spread.

## Phase 2 — Mutate (10 min)

- *"Add a third feature, days_since_last_order."* — Nothing changes in `linreg.py`; why not?
- *"Stop when the loss stops improving, not when the gradient is small."* — Which lines, named before typing.

## Phase 3 — Debug (10 min)

| Seed | Break | Probes |
|---|---|---|
| Easy | `X @ w` written `X * w` | Shape error — do they read the shapes? |
| Medium | `standardise` uses `axis=1` | Wrong numbers, no error; rows vs columns |
| Medium | Gradient missing the 2 | Still converges, more slowly — does the finite-difference check catch it? |
| Nasty | `intercept_ = b` (no un-standardising) | Fits, scores look plausible on standardised data, predictions on raw data are off by a constant |

The **Nasty** one: a model can be internally consistent and still wrong in the units
the caller uses. Check against the library on raw data.

---

## Scoring

| Phase | 5 | 3 | 1 |
|---|---|---|---|
| **Draw** | Both steps right, says why | One right | Cannot draw the loss |
| **Explain** | Confounding and base rate in their own words | Needs prompting | Recites |
| **Mutate** | Names every line before typing | Gets there | Cannot place the change |
| **Debug** | Suspects the silent one | Finds it | Guesses |

---

## Instructor: framing week 3

> **Monday the model stops predicting a number and starts predicting "will they leave?".**
> Same weighted sum, same gradient descent, one new squashing function — and suddenly
> accuracy is not enough.
