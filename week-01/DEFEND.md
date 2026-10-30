# Week 1 — Friday defence

Forty minutes. It starts with the student running `python prepare.py` on a fresh clone.

---

## Phase 0 — Live (5 min)

Fresh clone, `python week-01/milestone/prepare.py`, then read the report aloud — the
numbers must match what the script printed.

## Phase 1 — Explain (10 min)

1. *"Your rule is right 85.5% of the time. Is it good?"* — No: "nobody leaves" scores 86.95%. Accuracy without a baseline means nothing.
2. *"Why did you make the negative spends missing rather than zero?"* — Zero is a real spend and would drag the median down; impossible means unknown. This is the best question of the week.
3. *"Why fill with the plan's median and not the overall mean?"* — Spend depends on plan; the mean is pulled by large spenders.
4. *"cancel_reason predicts churn perfectly. Why throw away your best column?"* — It is written after the event; at prediction time it is empty for everyone.
5. *"Why must the order be impossible-then-fill?"* — Otherwise the -1s survive as real values and are never filled.

## Phase 2 — Mutate (10 min)

- *"Next month a spend over 10,000 is also impossible."* — One line in `fix_impossible`, named before typing.
- *"The export gains a column `refund_issued`, written after cancellation."* — Nothing changes: `find_leaks` catches it. Show it by adding the column.

## Phase 3 — Debug (10 min)

| Seed | Break | Probes |
|---|---|---|
| Easy | `read_csv` path typo | Reads the traceback bottom-up |
| Medium | `drop_duplicates()` without `subset` | Duplicate customers survive if any field differs; count changes |
| Medium | `.str.lower()` without `.str.strip()` | 5 regions instead of 4 — do they count unique values? |
| Nasty | Fill with the overall median *before* `fix_impossible` | No error, 2,000 rows, no NaN — but twelve customers now spend -1.0 |

The **Nasty** one: a clean-looking file with no missing values can still be wrong. Check
the range of a column, not just its gaps.

---

## Scoring

| Phase | 5 | 3 | 1 |
|---|---|---|---|
| **Live** | Runs first time; numbers match the report | Runs after a fix | Does not run |
| **Explain** | Baseline and leak in their own words | Needs prompting | Recites |
| **Mutate** | Names every line before typing | Gets there | Cannot place the change |
| **Debug** | Suspects the silent one | Finds it | Guesses |

---

## Instructor: framing week 2

> **Next week the computer will learn the threshold for you.** To trust it, you need
> to know what "learn" means: a slope, a step downhill, and a probability. Three days of
> maths, all of it in code, and on Thursday it fits a line.
