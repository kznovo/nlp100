from collections import Counter

with open("hightemp.txt") as f:
    text = f.read().strip().split("\n")

first_cnt = sorted(
    Counter(row.split("\t")[0] for row in text).items(),
    key=lambda x: x[1],
    reverse=True,
)
for pref, cnt in first_cnt:
    print(pref)
