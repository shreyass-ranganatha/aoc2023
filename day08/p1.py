from collections import defaultdict
from itertools import combinations
import re

def findpoints(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    dy = y2 - y1
    dx = x2 - x1

    if dx == 0:
        return (
            (x1, min(y1, y2) - abs(dy)),
            (x1, max(y1, y2) + abs(dy)))

    if dy == 0:
        return (
            (min(x1, x2) - abs(dx), y1),
            (max(x1, x2) + abs(dx), y1))

    if dy / dx < 0:
        return (
            (min(x1, x2) - abs(dx), max(y1, y2) + abs(dy)),
            (max(x1, x2) + abs(dx), min(y1, y2) - abs(dy)))

    else:
        return (
            (min(x1, x2) - abs(dx), min(y1, y2) - abs(dy)),
            (max(x1, x2) + abs(dx), max(y1, y2) + abs(dy)))


dt = defaultdict(set)
mp = []

with open("inputs/day08.txt") as fp:
    for j, l in enumerate(fp):
        l = l.strip()

        for m in re.finditer(r"[^\.]", l):
            dt[m.group()].add((m.start(), j))
        mp.append([*l])

h, w = len(mp), len(mp[0])
rs = set()

for k, ps in dt.items():
    for p1, p2 in combinations(ps, 2):
        p3, p4 = findpoints(p1, p2)

        if 0 <= p3[0] < w and 0 <= p3[1] < h:
            rs.add((p3[0], p3[1]))

        if 0 <= p4[0] < h and 0 <= p4[1] < h:
            rs.add((p4[0], p4[1]))

print(len(rs))
