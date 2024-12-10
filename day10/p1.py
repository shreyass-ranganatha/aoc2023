
def dfs(x, y):
    v = set()
    n = {(x, y)}

    ct = 0

    while n:
        x, y = n.pop()
        v.add((x, y))

        if mp[y][x] == 9:
            ct += 1
            continue

        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < len(mp) and
                0 <= ny < len(mp[0]) and
                (nx, ny) not in v
            ):
                if mp[ny][nx] - mp[y][x] == 1:
                    n.add((nx, ny))

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
    ct += dfs(*h)

print(ct)
