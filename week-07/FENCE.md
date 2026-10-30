# Week 7 — Concept fence

## Allowed

**Everything from weeks 1 to 6**, plus:

- tensors, `requires_grad`, `.backward()`, `torch.no_grad()`, `float32` vs `float64`
- `nn.Module`, `nn.Sequential`, `nn.Linear`, `nn.ReLU`, `nn.Dropout`
- `nn.CrossEntropyLoss`, `nn.BCEWithLogitsLoss`, `torch.optim.SGD`, `torch.optim.Adam`
- `TensorDataset`, `DataLoader`, `state_dict`, `copy.deepcopy`

## Not yet

convolution (week 8) · embeddings and recurrent layers (week 9) · batch normalisation · learning-rate
schedules · GPUs · PyTorch Lightning, Keras, skorch · saving with `torch.save` (week 12)

---

## Why no GPU

Every network in this course trains in under a few seconds on a laptop CPU, by design.
A GPU adds drivers, device bugs and `.to(device)` on every line, and teaches nothing about
why a network memorises. The ideas this week are the ones that decide whether a GPU's
hours are wasted: a validation set, a best epoch, a baseline the network has to beat.
