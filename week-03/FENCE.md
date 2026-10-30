# Week 3 — Concept fence

## Allowed

**Everything from weeks 1 and 2**, plus:

- the sigmoid and log loss; logistic regression by gradient descent
- broadcasting with `[:, None]`
- scikit-learn's `LogisticRegression` and `roc_auc_score` — **only** in tests, to check yours

## Not yet

trees and forests (week 4) · cross-validation and tuning (week 4) · regularisation (week 4) ·
`sklearn.metrics` in your own files · resampling and class weights · calibration

---

## Why no class weights or oversampling

Every tutorial on imbalanced data reaches for SMOTE or `class_weight="balanced"`. Here the
imbalance is handled by choosing a threshold from costs, because that is the decision the
shop actually makes — "who gets an offer?" — and it leaves the probabilities honest.
Reweighting changes the probabilities to move the threshold you could have moved directly.
