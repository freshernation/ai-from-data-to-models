"""Given, and run live only - transfer learning in one look.

    pip install torchvision          # not in requirements.txt: about 30 MB, plus 45 MB of weights
    python pretrained_live.py my_mug.jpg

Loads ResNet-18, trained on 1.2 million real photos (ImageNet), and prints its top five
guesses for your photo. Nothing in the tests runs this: it downloads weights.

Then try: what does a model trained on a million photos think of one of the shop's
16 x 16 icons? (python pretrained_live.py --icon)
"""

import sys

import torch


def main():
    from torchvision.models import ResNet18_Weights, resnet18
    weights = ResNet18_Weights.DEFAULT
    model = resnet18(weights=weights).eval()
    prep = weights.transforms()
    if sys.argv[1:] == ["--icon"]:
        from shoplab import images
        icon = torch.tensor(images.load()["X_test"][0] / 255.0, dtype=torch.float32)
        picture = icon[None].repeat(3, 1, 1)
    else:
        from torchvision.io import read_image
        picture = read_image(sys.argv[1])[:3].float() / 255.0
    with torch.no_grad():
        probs = model(prep(picture)[None]).softmax(1)[0]
    for p, i in zip(*probs.topk(5)):
        print(f"{p:6.1%}  {weights.meta['categories'][i]}")


if __name__ == "__main__":
    main()
