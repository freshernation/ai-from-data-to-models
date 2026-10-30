# AI From Data to Models

Twelve weeks from "I can write a Python function" to "I trained, measured and shipped
five kinds of model".

You know basic Python. This course takes one small online shop and builds its AI, one
model at a time: who is about to leave (tables), which customers are alike and what they
will buy next, what is in a product photo (images), what a review means (text), and when
an LLM does that better or worse than your own model. In the last week all of it runs
behind one API in Docker. Every model is built by hand first, then checked against
scikit-learn or PyTorch, and every number sits next to the baseline it has to beat.

---

## Who this is for

You can write functions, loops, dicts and a small class, read a traceback, and use git
— roughly the first four weeks of a Python course. You do **not** need numpy, pandas,
statistics, calculus or any machine learning yet; each arrives in the week that needs it.
Before week 1 you run a short baseline interview so that you, and your instructor, know
which to watch.

---

## The rules

**1. The twenty-minute rule.** Stuck for twenty minutes: open the tutor. Still stuck:
bring it to the live hour. Log every stuck moment in `logs/stuck-log.md`.

**2. You may not commit a line you could not have written and cannot explain on
Friday.**

**3. Nothing counts until the tests pass and it is pushed.**

**4. Every number goes next to its baseline, and the test set is touched once.** A model
that is "88% accurate" means nothing until you know predicting "nobody leaves" scores 87%.

---

## The twelve weeks

| Week | | Milestone |
|---|---|---|
| 1 | [Data before models](week-01/README.md) | The raw export cleaned, its leak found, and a data report |
| 2 | [The maths, in code](week-02/README.md) | Linear regression from scratch, matching scikit-learn |
| 3 | [A first classifier, honestly measured](week-03/README.md) | Churn v1 on a frozen test set, with a threshold chosen from costs |
| 4 | [**Trees, ensembles and tuning**](week-04/README.md) | **Project 1** — a churn model chosen by cross-validation, saved, with a model card |
| 5 | [Without labels](week-05/README.md) | Customer segments, and a recommender that beats "most popular" |
| 6 | [A neural network by hand](week-06/README.md) | An MLP and its backpropagation in numpy, gradient-checked |
| 7 | [PyTorch, properly](week-07/README.md) | A reusable training loop, and a network against every churn model so far |
| 8 | [**Images: CNNs**](week-08/README.md) | **Project 2** — a product-image classifier, stress-tested, with a model card |
| 9 | [Text: counts to sequences](week-09/README.md) | Review sentiment from word counts to an LSTM, and every mistake read |
| 10 | [Attention and transformers](week-10/README.md) | A small transformer, and a shuffle test of what each text model learned |
| 11 | [Generative AI](week-11/README.md) | A review-reply drafter: your model decides, an LLM writes, a guardrail stops the attacks |
| 12 | [**Ship it, defend it**](week-12/README.md) | **Project 3** — the shop's AI service: validated, fingerprinted, containerised, watched for drift; and a mock interview |

Every test runs offline on a laptop CPU. The data is in `data/`. No account or key is
needed until week 11, and even then the tests use a scripted fake model; a free-tier key
is optional for the live runs.

---

## How a week works

| | |
|---|---|
| **Monday to Thursday** | One live hour, then the day's folder: read, build, make the tests pass |
| **Friday** | No new content. Ship the milestone, then defend it |

Each day folder has a `README.md`, the files to write, and a test file that fails until
you have written them. Run the day's tests with `pytest week-NN/day-N -v`.

---

## What is in the repo

| Path | What it is |
|---|---|
| `shoplab/` | The shop: customers, orders, product photos and reviews, the frozen splits, and (week 11) the model client |
| `data/` | The shop's data files |
| `week-01/` … | One folder per week |
| `ai/` | The AI roles. Read `ai/README.md` first |
| `logs/` | Your baseline, your stuck log and your signal log |
| `SETUP.md` | Day zero |
| `CUT_LIST.md` | What this course does not teach, and why |
| `SOURCES.md` | What to read, and what to ignore |

Start with `SETUP.md`.
