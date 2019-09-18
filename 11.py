with open("hightemp.txt") as f:
    text = f.read()

processed = text.strip().replace("\t", " ")

print(processed)
