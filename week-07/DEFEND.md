# Week 7 — Friday defence

Forty minutes. It starts with a plot.

---

## Phase 0 — Draw (5 min)

Sketch the training and validation loss curves for the sixty-point network with no
regularisation. Mark the best epoch. Then sketch the same with weight decay.

## Phase 1 — Explain (10 min)

1. *"Your autograd gradients differ from week 6's by 1e-8. Is one wrong?"* — No: float32 holds about seven significant digits; in float64 they agree to 1e-16.
2. *"Validation loss went up fourteen-fold but accuracy fell only three points. How?"* — Loss punishes confidence; the memorising network is very sure of its wrong answers. Best question of the week.
3. *"Why does early stopping need a validation set and not the test set?"* — Choosing the epoch is a decision; decisions made on the test set make its score optimistic.
4. *"The network beats the line by 0.006 AUC. Ship it?"* — No: its own spread across seeds is 0.007, the test has 65 leavers, and the line is cheaper and explainable.
5. *"What does `model.eval()` change?"* — Dropout stops dropping; forgetting it makes validation noisy and worse.

## Phase 2 — Mutate (10 min)

- *"Use mini-batches of 64 in `trainer.fit`."* — Which lines change, and what does "epoch" now mean?
- *"Stop on validation AUC instead of loss."* — Where, and why the comparison flips direction.

## Phase 3 — Debug (10 min)

| Seed | Break | Probes |
|---|---|---|
| Easy | `optimiser.zero_grad()` missing | Gradients accumulate; loss erratic |
| Medium | `y` passed as float to CrossEntropyLoss | Error about dtype — do they read it? |
| Medium | `best_state = model.state_dict()` without deepcopy | The "best" state silently follows the model; restoring does nothing |
| Nasty | Validation computed in `model.train()` mode | No error; dropout makes validation loss noisy and early stopping picks a random epoch |

The **Nasty** one: one missing `.eval()` makes every number this week slightly wrong, and
nothing crashes.

---

## Scoring

| Phase | 5 | 3 | 1 |
|---|---|---|---|
| **Draw** | Both curves and the best epoch, with and without decay | One curve | Cannot draw them |
| **Explain** | Confidence vs accuracy, and noise vs gain | Needs prompting | "The network is better" |
| **Mutate** | Names every line before typing | Gets there | Cannot place the change |
| **Debug** | Suspects the silent one | Finds it | Guesses |

---

## Instructor: framing week 8

> **On the shop's table, the network tied the line.** Next week the data is pictures of
> products, and a line cannot even see that two photos of the same mug, one shifted a few
> pixels, are the same mug. That is where networks earn their keep.
