# Week 12 — Ship it, defend it (Project 3)

> **Destination**
> You can put every model you trained behind one validated API, prove which model files
> are running, package it in a container that does not run as root, detect when next
> month's customers no longer look like last month's, report a fairness number honestly —
> and defend all of it live, then in a mock interview.

Five models in eleven folders help nobody. This week they become one service: a
validated API, a manifest that fingerprints every model file, a container, and a drift
check. Then the shop's world changes — a reminder-email campaign nobody told the model
about — and you find out whether your monitoring notices before the customers do. The
week ends with the defence of the whole project and a mock interview.

---

## The week

| Day | Folder | What you'll be able to do |
|---|---|---|
| Mon | `day-1/` | Serve models behind FastAPI, and refuse input they were never trained on |
| Tue | `day-2/` | Fingerprint every model file and refuse to run anything changed |
| Wed | `day-3/` | Measure drift with PSI, recall by group, and explain one prediction |
| Thu | `day-4/` | Load-test the API, write your portfolio page, rehearse the interview |
| Fri | `milestone/` | **Project 3**: the shop's AI service, its Dockerfile, `REVIEW.md` — defended live |

---

## The rule from this week on

**A model in production is a model you are watching.** Version it, validate what goes
in, measure how fast it answers, and check every week that the world still looks like
its training data.

---

## Before Monday

Install Docker Desktop (free for personal use) and run `docker run hello-world`. The
tests do not need Docker; Friday's defence does.

---

## Outside-view question

> *A restaurant inspector arrives unannounced. What do they check first — and what would
> they never learn from the menu?*
