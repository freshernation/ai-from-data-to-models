# Week 3 — A first classifier, honestly measured

> **Destination**
> You can split data so the test set means something, train logistic regression from
> scratch to match scikit-learn, report precision, recall and AUC beside the baseline,
> and choose a threshold from what mistakes cost.

Week 1 showed that accuracy can call a useless rule good. Week 2 gave you a model that
learns. This week they meet: the first model that predicts "will they leave?" — and the
first week where a model can look worse on accuracy and still be the better choice.
Everything here is about measurement, because from week 4 on the models get clever
enough to fool you.

---

## The week

| Day | Folder | What you'll be able to do |
|---|---|---|
| Mon | `day-1/` | Split data randomly and stratified, and see how much an unlucky split moves the baseline |
| Tue | `day-2/` | Train logistic regression from scratch and match scikit-learn |
| Wed | `day-3/` | Compute a confusion matrix, precision, recall, F1 and ROC AUC by hand |
| Thu | `day-4/` | Pick the threshold that makes the most money |
| Fri | `milestone/` | Churn v1 on the frozen test set, and `EVAL.md` |

---

## The rule from this week on

**The test set is touched once, at the end.** Thresholds, settings and choices are made on
training data. From now on every model is scored on `shoplab.customers.frozen_split()`.

---

## Before Monday

Nothing new. From today you may use scikit-learn to *check* your code; you write the
code by hand.

---

## Outside-view question

> *A smoke alarm goes off every time someone makes toast. It has never missed a real fire.
> Is it accurate? Would you keep it?*
