import sys

n = int(sys.argv[1])

with open("hightemp.txt") as f:
    text = f.read().strip().split("\n")

div = len(text) // n
for i in range(0, len(text), div):
    print(text[i : i + div])
