with open("col1.txt") as col1, open("col2.txt") as col2:
    col1_text = col1.read()
    col2_text = col2.read()

merged = "\n".join(
    f"{c1}\t{c2}" for c1, c2 in zip(col1_text.split("\n"), col2_text.split("\n"))
)

with open("merged.txt", "w") as f:
    f.write(merged)
