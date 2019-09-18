import sys

n = int(sys.argv[1])

with open("hightemp.txt") as f:
    text = f.read()

tail_n = "\n".join(text.strip().split("\n")[-n:])

print(tail_n)
