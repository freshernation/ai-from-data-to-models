# Week 6 — A neural network by hand

> **Destination**
> You can show why one layer cannot learn XOR, write a two-layer network's forward and
> backward pass in numpy, prove your gradients right to eleven decimal places, and train
> it to beat a straight line on data a line cannot separate.

Every model so far was one layer of arithmetic: a weighted sum, perhaps squashed. This
week you stack two, and meet the reason it took the field decades to train the stack: the
error has to travel backwards through every layer to tell each weight which way to move.
You write that by hand, once, so that next week, when PyTorch does it in one line, you know
exactly what the line does.

---

## The week

| Day | Folder | What you'll be able to do |
|---|---|---|
| Mon | `day-1/` | Train a perceptron and watch it fail on XOR |
| Tue | `day-2/` | Write relu, softmax, cross-entropy and a forward pass, and solve XOR with hand-set weights |
| Wed | `day-3/` | Write backpropagation and check it against finite differences |
| Thu | `day-4/` | Train the network, and break it with zero weights and a large step |
| Fri | `milestone/` | An `MLP` class in numpy that beats a line on two moons, and `NOTES.md` |

---

## The rule from this week on

**A gradient you have not checked is a guess.** Every hand-written gradient is compared
with a finite difference before it is used to train anything.

---

## Before Monday

Nothing new. Re-read week 2 day 2: this week is its chain rule, applied twice.

---

## Outside-view question

> *How does a child learn to ride a bike? What is the "error", and how does it reach the
> part of them that needs to change?*
