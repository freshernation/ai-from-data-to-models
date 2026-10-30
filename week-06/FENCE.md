# Week 6 — Concept fence

## Allowed

**Everything from weeks 1 to 5**, plus:

- the perceptron rule; relu, softmax, cross-entropy
- forward and backward passes by hand in numpy; `np.ndindex`
- He initialisation; full-batch gradient descent
- `sklearn.datasets.make_moons`; scikit-learn's `LogisticRegression` as the baseline

## Not yet

PyTorch and autograd (week 7) · mini-batches and optimisers like Adam (week 7) · dropout and weight
decay (week 7) · `MLPClassifier` · more than one hidden layer · convolution (week 8)

---

## Why no autograd yet

PyTorch computes every gradient in this week for you, correctly, in one call. Writing them
by hand is slower and more error-prone, which is the point: the bugs you meet on Wednesday
— a missing 1/n, a relu that passes gradient where it was off — are the bugs that make a
real network train badly without crashing. Someone who has found them by hand recognises
them in a loss curve; someone who has only called `.backward()` does not.
