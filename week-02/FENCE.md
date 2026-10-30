# Week 2 — Concept fence

## Allowed

**Everything from week 1**, plus:

- `@`, `.T`, `np.column_stack`, `np.linalg.solve`, `np.errstate`, `axis=`
- `np.random.default_rng`
- `math.exp`, `math.sqrt`, `math.pi`
- scikit-learn's `LinearRegression` — **only** to check yours in the milestone

## Not yet

classification (week 3) · regularisation (week 4) · stochastic / mini-batch gradient descent (week 7) ·
`np.linalg.inv` · `np.polyfit` · symbolic maths (sympy) · proofs

---

## Why no matrix inverse

The normal equation is written with an inverse in every textbook, and `np.linalg.inv`
would pass the tests. It is banned because inverting is slower and less accurate than
solving, and because a student who types `inv` has learned a formula, while one who
calls `solve` has learned that fitting a line is solving a system of equations.
