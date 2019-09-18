with open("hightemp.txt") as f:
    text = f.read().strip().split("\n")

first = {row.split("\t")[0] for row in text}
for pref in first:
    print(pref)
