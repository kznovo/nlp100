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
top_10 = cnt_sorted[:10]
print(top_10)

plt.rcdefaults()
plt.rcParams["font.family"] = "Hiragino Maru Gothic Pro"
fig, ax = plt.subplots()
words = [t[0] for t in top_10]
y_pos = np.arange(len(words))
counts = [t[1] for t in top_10]
ax.barh(y_pos, counts, align="center")
ax.set_yticks(y_pos)
ax.set_yticklabels(words)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel("出現頻度")
ax.set_title("上位１０語")

plt.show()
