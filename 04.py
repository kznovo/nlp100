string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

tops = (1, 5, 6, 7, 8, 9, 15, 16, 19)

res = {}
for i, s in enumerate(string.split(), 1):
    if i in tops:
        s = s[0]
    else:
        s = s[:2]
    res[s] = i

print(res)
