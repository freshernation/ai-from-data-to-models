# Day 1 — One API for every model

> **By the end of today** you can serve models behind FastAPI with typed, range-checked
> input, and show that broken input never reaches a model.

---

## Read first

- [ ] FastAPI — [Request body](https://fastapi.tiangolo.com/tutorial/body/) · 15 min
- [ ] Pydantic — [Fields](https://docs.pydantic.dev/latest/concepts/fields/) — "Numeric constraints" and "String constraints" · 10 min

---

## What you need to know

### Models as plain functions

`create_app(churn, sentiment, product)` takes three functions. Today you test it with
stand-ins; on Friday you pass the real models. The API does not know or care what is
behind each function — which is what lets you swap a model without touching the API.

### Validate at the door

A pydantic model describes what a request must contain: `tenure_months: int =
Field(ge=1, le=120)`, `plan: Literal["basic", "plus", "pro"]`. FastAPI checks every
request against it and answers **422** with the reason if it fails.

### The finding

Five broken customers — a tenure of 0, an unknown plan, a discount of 2, a negative spend,
a missing field — get five 422s, and the model is called **zero** times. A model trained
on tenures from 1 to 60 has no idea what a tenure of 0 means; its answer would be
invented. Refusing is the honest response.

---

## Exercises

```bash
pytest week-12/day-1 -v
```

Write the three request models and `create_app` in `api.py`. Then run it with stand-ins:
`uvicorn` and open `/docs`.

---

## Predict-then-run

What does FastAPI return for a review of 600 characters — before your code runs at all?

---

## Before you close the laptop

Commit, push, fill in the signal log.
