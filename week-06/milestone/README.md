# Week 6 Milestone — A network by hand

> An `MLP` class in numpy, gradient-checked, that beats a straight line on two noisy
> moons, and `NOTES.md` explaining what you built in your own words.

---

## The files

| File | Where it comes from |
|---|---|
| `forward.py` | **copy** from `day-2/` |
| `backprop.py` | **copy** from `day-3/` |
| `mlp.py` | new: the `MLP` class; `moons()` is given |
| `NOTES.md` | new |

## `NOTES.md`

| Section | What goes in it |
|---|---|
| Why one layer is not enough | XOR, and your perceptron's history |
| What backpropagation does | In words, no formulas needed |
| How I know my gradients are right | The check and its numbers |
| Why the starting weights matter | Zero vs He, and the step size |
| What the hidden layer bought | Your MLP against the line on moons |

At least 50 words each.

---

## Check it

```bash
pytest week-06/milestone -v
```

## Friday

You draw the network with every shape, forwards and backwards.
