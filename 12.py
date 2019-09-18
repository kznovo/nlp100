with open("hightemp.txt") as f:
    text = f.read()

col1, col2 = [], []
for row in text.strip().split("\n"):
    cols = row.split("\t")
    col1.append(cols[0])
    col2.append(cols[1])

col1_text = "\n".join(col1)
col2_text = "\n".join(col2)

with open("col1.txt", "w") as f:
    f.write(col1_text)

with open("col2.txt", "w") as f:
    f.write(col2_text)
