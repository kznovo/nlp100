from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


def load_neko_txt_mecab():
    with open("neko.txt.mecab") as f:
        text = f.read().strip()
    sentences = []
    for row in text.split("\n"):
        if row == "EOS":
            continue
        surface, analysis = row.split("\t")
        arr = analysis.split(",")
        sentences.append(
            {"surface": surface, "base": arr[6], "pos": arr[0], "pos1": arr[1]}
        )
    return sentences


neko_txt = load_neko_txt_mecab()

cnt = Counter(tag["surface"] for tag in neko_txt)
cnt_sorted = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

plt.hist([t[1] for t in cnt_sorted])
plt.show()
