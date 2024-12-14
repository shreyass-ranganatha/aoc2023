import numpy as np
import re

nps = []
h = w = 0

with open("inputs/day14.txt") as fp:
    for l in fp:
        (px, py, vx, vy), = re.findall(
            r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)",
            l.strip())

        h = max(h, int(py))
        w = max(w, int(px))

        nps.append([int(px), int(py), int(vx), int(vy)])

mp = np.zeros((h+1, w+1))
steps = 100

for px, py, vx, vy in nps:
    y = (py + vy * steps) % (h + 1)
    x = (px + vx * steps) % (w + 1)

    mp[y, x] += 1

sm = (
    mp[:h//2, :w//2].sum() * mp[:h//2, -w//2:].sum() *
    mp[-h//2:, :w//2].sum() * mp[-h//2:, -w//2:].sum())

print(int(sm))
