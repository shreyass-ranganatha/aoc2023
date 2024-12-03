import re

with open("inputs/day03.txt") as fp:
    tx = fp.read().strip()

sm = 0
fg = 1

for r in re.finditer(
    r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))",
    tx
):
    c, a, b = r.groups()

    if c == "don't()":
        fg = 0
    elif c == "do()":
        fg = 1
    elif fg:
        sm += int(a) * int(b)

print(sm)
