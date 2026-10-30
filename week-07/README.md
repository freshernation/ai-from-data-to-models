# Week 7 — PyTorch, properly

> **Destination**
> You can reproduce week 6's gradients with autograd, train any network with a
> `DataLoader` and an optimiser, show a network memorising sixty points and stop it three
> ways, and say — with numbers — whether a network beats week 4's models on the shop's customers.

Last week you wrote backpropagation by hand. This week it becomes one line,
`loss.backward()`, and you get to spend the time on what actually goes wrong with real
networks: they are bigger than their data, and they memorise it. The week ends with an
honest question: on the shop's churn table, is any of this worth it?

---

## The week

| Day | Folder | What you'll be able to do |
|---|---|---|
| Mon | `day-1/` | Rebuild week 6's network in torch and match its gradients |
| Tue | `day-2/` | Write a module, a data loader and a training loop; see what mini-batches buy |
| Wed | `day-3/` | Watch a network memorise, and stop it with dropout, weight decay and early stopping |
| Thu | `day-4/` | Train a churn network and set it beside the line and the forest |
| Fri | `milestone/` | `trainer.py`, the loop weeks 8-10 use, and `COMPARISON.md` |

---

## The rule from this week on

**A validation set is carved from the training data, and the best epoch is chosen on it.**
Never on the test set — and never "the last epoch" by default.

---

## Before Monday

PyTorch is already installed (`requirements.txt`). Check: `python -c "import torch; print(torch.__version__)"`.

---

## Outside-view question

> *A sports coach changes an athlete's training plan and their times improve. How does the
> coach know it was the plan, and not just the athlete getting older, fitter or luckier?*
