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
res = [
    tag["surface"] for tag in neko_txt if tag["pos1"] == "サ変接続" and tag["pos"] == "名詞"
]

print(res[:10])
