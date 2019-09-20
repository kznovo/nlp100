from typing import Dict


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

res = []
prev = {}  # type: Dict[str, str]
no = False
for tag in neko_txt:
    if no:
        if prev.get("pos", "") == "名詞" and tag["pos"] == "名詞":
            res.append(f"{prev['surface']}の{tag['surface']}")
        no = False
    else:
        if tag["surface"] == "の":
            no = True
        else:
            prev = tag

print(res[:10])
