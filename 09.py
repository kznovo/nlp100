import random


def typoglycemia(string: str) -> str:
    res = []
    for s in string.split():
        if len(s) > 4:
            mid = s[1:-1]
            shuffled = "".join(random.sample(mid, len(mid)))
            s = s[0] + shuffled + s[-1]
        res.append(s)
    return " ".join(res)


string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(string))

