with open("hightemp.txt") as f:
    text = f.read().strip().split("\n")

seq = sorted(text, key=lambda x: x.split("\t")[2], reverse=True)
for s in seq:
    print(s)
