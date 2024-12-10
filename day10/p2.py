from collections import Counter

def dfs(x, y):
    n = {(x, y, ())}
    ct = Counter()

    while n:
        x, y, v = n.pop()
        v += (x, y)

        if mp[y][x] == 9:
            ct[(y, x)] += 1
            continue

        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < len(mp) and
                0 <= ny < len(mp[0]) and
                (nx, ny) not in v
            ):
                if mp[ny][nx] - mp[y][x] == 1:
                    n.add((nx, ny, v))

    return ct

heads = []
mp = []

with open("inputs/day10.txt") as fp:
    for j, l in enumerate(fp):
        l = [*map(int, l.strip())]

        if 0 in l:
            for i in range(len(l)):
                if l[i] == 0:
                    heads.append((i, j))
        mp.append(l)

ct = 0
for h in heads:
    ct += dfs(*h).total()

print(ct)
