def cipher(string: str):
    return "".join(chr(219 - ord(s)) if "a" <= s <= "z" else s for s in string)


string = "My name is Kazuya Hatta"
ciphered = cipher(string)
print(ciphered)
deciphered = cipher(ciphered)
print(deciphered)
