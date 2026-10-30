# Week 5 Milestone — Segments and "also bought"

> Three customer segments with profiles, a recommender with "also bought" and per-customer
> suggestions, and `SEGMENTS.md` for the marketing lead.

---

## The files

| File | Where it comes from |
|---|---|
| `kmeans.py` | **copy** from `day-1/` |
| `recommend.py` | **copy** from `day-3/` |
| `shop_recs.py` | new: `segment_customers()` and `Recommender` |
| `SEGMENTS.md` | new |

## `SEGMENTS.md`

| Section | What goes in it |
|---|---|
| The segments | Each segment's size and what it buys |
| Why three and not four | The elbow and the purity, in plain words |
| What the recommender adds | "Also bought", and the hit rates |
| How I know it works | How the evaluation hid data from itself |
| What I would not use it for | Its blind spots |

At least 50 words each.

---

## Check it

```bash
pytest week-05/milestone -v
python week-05/milestone/shop_recs.py
```

## Friday

You draw the customers on PCA's two axes before seeing the plot.
