from typing import List, Sequence


def get_ngram(seq: Sequence[str], n: int):
    res = []
    for i in range(len(seq) - n + 1):
        gram = seq[i : i + n]
        res.append(gram)
    return res


string = "I am an NLPer"
print(get_ngram(string.split(), 2))
print(get_ngram(string, 2))
