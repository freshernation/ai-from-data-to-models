# Week 12 — Friday defence: Project 3, and the interview

Ninety minutes: forty for the defence, fifty for the mock interview.

---

## Phase 0 — Live (10 min)

From a fresh clone: `python week-12/milestone/train_all.py`, then
`docker build -f week-12/milestone/Dockerfile -t shop-ai .` and `docker run -p 8000:8000 shop-ai`.
Open `/docs`. The instructor sends one customer, one review and one photo of their choice,
then 300 of next month's customers to `/drift`. Then change one byte of `bundle/product.pt`
and restart.

## Phase 1 — Explain (10 min)

1. *"/drift says one column drifted. Is the model broken?"* — The email changed what days-since-last-order means; recall fell from 71% to 45% while churn did not move. Retrain on new data; the model was right about the old world. Best question of the week.
2. *"Your pro customers get 0% recall. Is the model unfair to them?"* — There is one pro leaver in the test set; the number is noise. Report counts beside every group rate.
3. *"Why reject a tenure of 0 instead of predicting anyway?"* — The model never saw one; its answer would be made up. A 422 is honest.
4. *"What does the manifest protect you from?"* — Running weights nobody evaluated: a half-copied file, a wrong version, an edit.
5. *"Churn is your slowest endpoint. Why?"* — It builds a pandas table per request; the model itself is a dot product.

## Phase 2 — Mutate (10 min)

- *"Add `/recommend` from week 5."* — Which files, which bundle entry, which manifest line?
- *"The shop wants a retrain when any column passes PSI 0.25."* — Where does that check live, and who runs it?

## Phase 3 — Debug (10 min)

| Seed | Break | Probes |
|---|---|---|
| Easy | `uvicorn serve:app` without `--host 0.0.0.0` | Runs in the container, unreachable from outside |
| Medium | `requirements-serve.txt` missing matplotlib | Import error at start-up — read the container logs |
| Medium | `COPY` of code before `pip install` | Works; every code change reinstalls torch — they time two builds |
| Nasty | `reference.csv` written from the TEST customers | No error; drift numbers shift slightly; the reference is no longer what the model learned from |

The **Nasty** one: the comparison is only as honest as its reference.

---

## Scoring

| Phase | 5 | 3 | 1 |
|---|---|---|---|
| **Live** | Builds, runs, every request answered, tampering caught | Runs with help | Does not run |
| **Explain** | Drift vs a broken model, and counts beside rates | Needs prompting | "Accuracy is 98%" |
| **Mutate** | Names every file and line before typing | Gets there | Cannot place the change |
| **Debug** | Suspects the silent one | Finds it | Guesses |

---

## The mock interview (50 min)

Run `ai/interviewer.md` live, the instructor as the interviewer, with the student's
`PORTFOLIO.md` as the project. Score design, debug and judgement out of 5 each, and record
the weakest answer in the student's signal log.

---

## Instructor: after the course

> **They can take raw data to a measured, shipped model and say what its numbers mean.**
> Point each student at the next course their weakest week suggests: `fine-tuning` after
> weeks 10-11, `RAG` after week 9, `agent-in-production` after week 12.
