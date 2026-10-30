# Day 4 — How fast, for whom, and the page you link from your CV

> **By the end of today** you can load-test your API and report its tail latency, and you
> have written the portfolio page the interview will be about.

---

## Read first

- [ ] Google — [Site Reliability Engineering: monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/) — "The four golden signals" and "Worrying about your tail" · 15 min
- [ ] `ai/interviewer.md` in this repo — the whole file · 5 min

---

## What you need to know

### Percentiles, not averages

The median (p50) is a typical customer. p95 is the slowest one in twenty; p99 the
slowest in a hundred. An average hides them all. On the author's laptop, the full
service answered churn in 6.3 ms at p50 and 7.9 ms at p95, sentiment in 4.0 and 4.3 ms.
Your numbers depend on your machine; the shape is what to look at.

### The portfolio page

`PORTFOLIO.md` is three minutes for a hiring manager: what you built, a table of results
each beside its baseline, the decision you are proudest of, what went wrong, and how to
run it. Every number in it is one you measured this term.

### The interview

Paste `ai/interviewer.md` with your portfolio and rehearse twice before Friday. It runs a
design question, a broken result to debug, and questions about your judgement.

---

## Exercises

```bash
pytest week-12/day-4 -v
```

Copy `api.py`, then write `load_test.py`, then write `PORTFOLIO.md`.

---

## Predict-then-run

Which endpoint will be slowest in your full service on Friday — the CNN, the LSTM or the
logistic regression? Write it down; check it in the milestone.

---

## Before you close the laptop

Commit, push, fill in the signal log. Then start Project 3.
