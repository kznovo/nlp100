string1 = "paraparaparadise"
string2 = "paragraph"

X = {string1[i : i + 2] for i in range(len(string1) - 1)}
Y = {string2[i : i + 2] for i in range(len(string2) - 1)}

sums = X | Y
diff = X - Y

se_in_X = "se" in X
se_in_Y = "se" in Y

print(sums)
print(diff)
print(se_in_X)
print(se_in_Y)
