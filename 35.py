from typing import List


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

res = []  # type: List[str]
tmp = []  # type: List[str]
for tag in neko_txt:
    if tag["pos"] != "名詞":
        if len(tmp) > len(res):
            res = tmp
        tmp = []
    else:
        tmp.append(tag["surface"])

print(res[:10])
