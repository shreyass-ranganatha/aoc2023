from collections import defaultdict
from itertools import combinations
import re

def findpoints(p1, p2, sz):
    x1, y1 = p1
    x2, y2 = p2
    h, w = sz

    dy = y2 - y1
    dx = x2 - x1

    rs = {p1, p2}

    if dx == 0:
        for i in range(min(y1, y2), -1, -abs(dy)):
            rs.add((x1, i))

        for i in range(max(y1, y2), h, abs(dy)):
            rs.add((x1, i))

    if dy == 0:
        for i in range(min(x1, x2), -1, -abs(dx)):
            rs.add((i, y1))

        for i in range(max(x1, x2), w, abs(dx)):
            rs.add((i, y1))

    if dy / dx < 0:
        i = 0
        while (
            0 <= (x := min(x1, x2) - abs(dx) * i) < w and
            0 <= (y := max(y1, y2) + abs(dy) * i) < h
        ):
            rs.add((x, y))
            i += 1

        i = 0
        while (
            0 <= (x := max(x1, x2) + abs(dx) * i) < w and
            0 <= (y := min(y1, y2) - abs(dy) * i) < h
        ):
            rs.add((x, y))
            i += 1

    else:
        i = 0
        while (
            0 <= (x := min(x1, x2) - abs(dx) * i) < w and
            0 <= (y := min(y1, y2) - abs(dy) * i) < h
        ):
            rs.add((x, y))
            i += 1

        i = 0
        while (
            0 <= (x := max(x1, x2) + abs(dx) * i) < w and
            0 <= (y := max(y1, y2) + abs(dy) * i) < h
        ):
            rs.add((x, y))
            i += 1

    return rs

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
        rs.update(findpoints(p1, p2, (h, w)))

print(len(rs))
