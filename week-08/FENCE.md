# Week 8 — Concept fence

## Allowed

**Everything from weeks 1 to 7**, plus:

- convolution and max pooling by hand; `nn.Conv2d`, `nn.MaxPool2d`, `nn.Flatten`, `.amax`
- data augmentation by shifting (`np.roll`); confusion matrices
- `torch.save` / `torch.load` of a `state_dict`
- `torchvision` — **only** in the given `pretrained_live.py`, run live

## Not yet

object detection and bounding boxes · batch normalisation · ResNets and skip connections in your own
code · fine-tuning a pretrained model in tests · OpenCV · colour images · GPUs

---

## Why synthetic 16 × 16 icons, not real photos

Real product photos need downloads, licences, gigabytes and a GPU, and a test suite that
cannot run offline. The icons keep every idea — filters, pooling, shift, augmentation,
breaking under noise — and train in four seconds. The cost is honesty about what the
scores mean, which is why the model card has a section on where the model breaks and why
Thursday shows a real pretrained network live.
