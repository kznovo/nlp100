with open("hightemp.txt") as f:
    text = f.read()

processed = text.strip().split("\n")
length = len(processed)

print(length)
