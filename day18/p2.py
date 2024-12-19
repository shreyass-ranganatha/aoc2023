import numpy as np

def n4(x, y):
    return [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]

def scan():
    h, w = mp.shape
    ns = [(0, 0, 0)]
    vs = set()

    while ns:
        x, y, d = ns.pop(0)

        if (x, y) in vs:
            continue
        vs.add((x, y))

        if not (0 <= x < w and 0 <= y < h):
            continue

        if mp[y][x] == '#':
            continue

        if y == h-1 and x == w-1:
            return 1

        for nx, ny in n4(x, y):
            ns.append((nx, ny, d+1))
    else:
        return 0

mp = np.zeros((71, 71), dtype=str)
mp.fill('.')

with open("inputs/day18.txt") as fp:
    for i, l in enumerate(fp):
        x, y = l.strip().split(',')
        mp[int(y)][int(x)] = '#'

        if i > 1024 and not scan():
            print(x, y, sep=',')
            break
