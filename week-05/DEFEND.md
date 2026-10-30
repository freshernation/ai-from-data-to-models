# Week 5 — Friday defence

Forty minutes. It starts with a drawing.

---

## Phase 0 — Draw (5 min)

Draw what the 2,000 customers look like on PCA's two axes — before showing any plot.
Where are the three groups? Where are the customers who buy everything?

## Phase 1 — Explain (10 min)

1. *"The shop has four kinds of customer. Why did you ship three segments?"* — The elbow says three; the browsers are a cloud between the others, not a cluster. A method can only find what has a shape. Best question of the week.
2. *"How do you know your recommender works with no labels?"* — Each customer's last purchase was hidden before building it; it finds 73% in the top ten against 31% for popular.
3. *"Why run k-means ten times?"* — It depends on the starting centroids and can stop in a worse arrangement; keep the lowest inertia.
4. *"Why does inertia always fall as k grows?"* — More centroids, every point closer; at k = n it is zero. You look for the bend, not the minimum.
5. *"What can this recommender never do?"* — Recommend an item nobody has bought; it only knows co-purchases.

## Phase 2 — Mutate (10 min)

- *"Recommend only items under 20."* — Where does the filter go, and does the hit-rate test still mean anything?
- *"Exclude the browsers from segmentation."* — How would you find them without the answer key?

## Phase 3 — Debug (10 min)

| Seed | Break | Probes |
|---|---|---|
| Easy | `assign` takes `argmax` | Inertia climbs; clusters nonsense |
| Medium | Cosine divides rows, not columns | Customer similarity instead of item similarity; recommendations odd |
| Medium | `recommend` forgets to exclude owned items | Hit rate unchanged on held-out items, but customers see what they own |
| Nasty | `hit_rate` builds the matrix from ALL orders, not history | No error; hit rate jumps to near 100%; the held-out item was in the matrix |

The **Nasty** one: the evaluation leak again, now with no label in sight.

---

## Scoring

| Phase | 5 | 3 | 1 |
|---|---|---|---|
| **Draw** | Three clouds and a smear between them | Three clouds | Cannot draw it |
| **Explain** | Explains "three not four" with the curve and purity | Needs prompting | "The elbow is at four" |
| **Mutate** | Names every line before typing | Gets there | Cannot place the change |
| **Debug** | Suspects the silent one | Finds it | Guesses |

---

## Instructor: framing week 6

> **Every model so far was one layer of arithmetic.** Next week you stack them, and find
> out why it took the field thirty years to train the stack: the gradient has to travel
> backwards through every layer. You will write that by hand.
