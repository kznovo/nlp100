import gzip
import json
import re

with gzip.open("jawiki-country.json.gz") as f:
    for line in f:
        data = json.loads(line)
        if data["title"] == "イギリス":
            text = data["text"]
            break

category_name = re.compile(r"^.*\[\[Category:(.*)(?:\|.*)?\]\].*$", re.MULTILINE)
result = category_name.findall(text)
for line in result:
    print(line)
