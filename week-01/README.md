# Week 1 — Data before models

> **Destination**
> You can take the shop's raw customer export, count every fault in it, fix each one,
> find the column that leaks the answer, and hand over a clean file and a report with
> your numbers in it.

Every model in this course trains on data someone else exported. This week you train
nothing. You measure the simplest possible "model" — a rule a manager wrote — against
the simplest possible baseline, and then spend three days finding out what is wrong with
the data. A leak found now is a lesson. Found in week 4, it is a lie in your model card.

---

## The week

| Day | Folder | What you'll be able to do |
|---|---|---|
| Mon | `day-1/` | Score a hand-written rule against "nobody leaves", with numpy and no loops |
| Tue | `day-2/` | Ask a table questions with pandas: rates, groups, top-N |
| Wed | `day-3/` | Remove duplicates, fix spellings, mark impossible values, fill gaps, and count each one |
| Thu | `day-4/` | Plot a distribution, compute rates by bucket, and find a leaking column |
| Fri | `milestone/` | `prepare.py` and `DATA_REPORT.md`, then the defence |

---

## The rule from this week on

**Every number you report sits next to its baseline.** "86% accurate" means nothing
until you know that predicting "nobody leaves" scores 86.95%.

---

## Before Monday

Finish `SETUP.md`. Nothing else is needed: the data is in `data/`, and every test runs offline.

---

## Outside-view question

> *A triage nurse sorts patients before any test has come back. What do they look at
> first, and what do they refuse to trust?*
