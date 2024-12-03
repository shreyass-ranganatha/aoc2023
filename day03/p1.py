import re

with open("inputs/day03.txt") as fp:
    tx = fp.read().strip()

sm = 0
for r in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", tx):
    a, b = r.groups()
    sm += int(a) * int(b)
print(sm)
