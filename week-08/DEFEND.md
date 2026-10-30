# Week 8 — Friday defence

Forty minutes. It starts with the saved model.

---

## Phase 0 — Live (5 min)

In a fresh Python session, load `product_classifier.pt`, take a test photo, move it four
pixels with `np.roll`, and predict both. Then darken it to 30% and predict again.

## Phase 1 — Explain (10 min)

1. *"The dense network has twelve times the weights. Why does it lose?"* — It learns each pixel position separately; the CNN shares one filter across positions and takes the max over the image. Best question of the week.
2. *"Augmentation fixed the dense network. So why a CNN?"* — The dense network had to be shown every position; the CNN gets it by design, with fewer weights and less data.
3. *"Your model is 100% on both test sets. What does the model card say?"* — Where it breaks: noise 0.6 → 50%, 30% brightness → 52%; and that the data is synthetic.
4. *"What does `.amax(dim=(2, 3))` do, and what if you removed it?"* — Takes each channel's strongest response anywhere; without it you would need a Linear over positions, and position would matter again.
5. *"Why save the state_dict and not the model?"* — Weights only; the class is in your code, so loading does not depend on pickled code.

## Phase 2 — Mutate (10 min)

- *"Add a fifth product, a lamp."* — Which lines change (classes, head, data)?
- *"Train with brightness augmentation too."* — Where in `augment`, and which stress number should move?

## Phase 3 — Debug (10 min)

| Seed | Break | Probes |
|---|---|---|
| Easy | `as_float` skipped: uint8 into the network | dtype error — do they read it? |
| Medium | Kernel flipped in `convolve2d` | The EDGE kernel is symmetric, so the PyTorch check still passes; only the small asymmetric test catches it |
| Medium | `load` without `model.eval()` | Harmless here (no dropout) — do they know why? |
| Nasty | Augmentation shifts the image but the labels are shuffled with a separate permutation | No error; accuracy falls to about chance on everything, training "runs" |

The **Nasty** one: misaligned data and labels train happily.

---

## Scoring

| Phase | 5 | 3 | 1 |
|---|---|---|---|
| **Live** | Loads, moves, darkens, predicts; explains each | Loads and predicts | Cannot load |
| **Explain** | Weight sharing and the max, in their own words | Needs prompting | "CNNs are better at images" |
| **Mutate** | Names every line before typing | Gets there | Cannot place the change |
| **Debug** | Suspects the silent one | Finds it | Guesses |

---

## Instructor: framing week 9

> **"Not bad at all" contains the word "bad".** Next week the shop's reviews arrive, and
> the model you know best — week 3's line, on word counts — reads them one word at a time.
> You will measure exactly how often that goes wrong.
