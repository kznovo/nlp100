string1 = "パトカー"
string2 = "タクシー"

combined = "".join(a + b for a, b in zip(string1, string2))

print(combined)
