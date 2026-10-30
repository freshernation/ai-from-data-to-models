# What this course does not teach

Every item below is real, and every one is out.

| Out | Why, and when to pick it up |
|---|---|
| **Python basics, data structures and algorithms** | The prerequisite. Algorithm puzzles are interview practice, not machine learning |
| **TensorFlow and Keras** | One framework learned properly. After week 7, Keras 3 reads the same in an afternoon |
| **GPUs and CUDA** | Every lab trains in seconds on a laptop CPU. The `fine-tuning` course needs a GPU and starts there |
| **Object detection (YOLO), real-time video, OpenCV** | Needs boxes drawn on thousands of images and a GPU. After week 8, the Ultralytics docs |
| **Face recognition** | Biometric data, with laws and harms of its own. Not taught here |
| **Time-series forecasting** | The network is week 9's; the hard part is validating across time, a course of its own |
| **Training GANs and diffusion models** | Week 11 explains how they generate. Training one is research-level |
| **Reinforcement learning** | A different problem shape, and nothing in the shop needs it. After the course, Sutton and Barto |
| **AutoML** | It automates exactly the choices weeks 3 and 4 teach you to make and defend |
| **Fine-tuning LLMs** | The `fine-tuning` course |
| **Retrieval (RAG) and agents** | The `RAG` and `agent` courses |
| **Cloud deployment and CI/CD** | The `agent-in-production` course. Week 12 stops at a Docker image |
| **"The future of AI", AGI** | Not something anyone can check. One outside-view question instead |

---

## Why

Each of these is learnable in about a week once you can take raw data to a model you
have measured honestly and shipped — and none of them teaches you to. People who know
why something was cut stop worrying that they are missing it.

---

## The one that will be argued about

**TensorFlow and Keras.** Plenty of job adverts name them, and Keras is gentler on day
one. But a course that teaches two frameworks teaches each half as well, and the ideas —
tensors, autograd, a module, a training loop — are the same in both. PyTorch is the one
most research and most open models use. The honest concession: if your first job uses
Keras, you will spend a few days on its API; you will not spend them on the ideas.

---

## What to add afterwards, in order

1. **Fine-tuning** — you will have built a transformer; adapting a real one is the next step.
2. **Retrieval (RAG)** — week 9's embeddings and week 5's similarity, at scale.
3. **Agents** — week 11's LLM client, given tools.
4. **Production** — week 12's container, deployed, monitored and updated.
