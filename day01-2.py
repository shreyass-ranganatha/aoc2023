import re

ns1 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ns2 = [_[::-1] for _ in ns1]

sm = 0

with open("inputs/day01.txt") as f:
    for ln in f:
        ln = ln.strip()

        a, *_ = re.findall("({})".format("|".join(ns1 + [r'\d'])), ln)
        if not a[0].isdigit():
            a = str(ns1.index(a) + 1)

        b, *_ = re.findall("({})".format("|".join(ns2 + [r'\d'])), ln[::-1])
        if not b[0].isdigit():
            b = str(ns2.index(b) + 1)

        sm += int(a+b)
print(sm)