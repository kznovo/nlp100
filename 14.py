import sys

n = int(sys.argv[1])

with open("hightemp.txt") as f:
    text = f.read()

top_n = "\n".join(text.split("\n")[:n])

print(top_n)
