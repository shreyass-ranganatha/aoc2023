
def turn(d):
    return -d[1], d[0]

def step(x, y, d):
    dx, dy = d
    return x+dx, y+dy

def navigate(x, y, d, b):
    ign = set()

    while 0 < x < w-1 and 0 < y < h-1:
        if (x, y, d) in vis or (x, y, d) in ign:
            return 1

        ign.add((x, y, d))
        xn, yn = step(x, y, d)

        if mp[yn][xn] == '#' or ((xn, yn) == b):
            d = turn(d)
        else:
            x, y = step(x, y, d)
    return 0

with open("inputs/day06.txt") as fp:
    mp = []

    for j, l in enumerate(fp):
        l = l.strip()

        if '^' in l:
            x, y = l.index('^'), j
        mp.append([*l])

h, w = len(mp), len(mp[0])
d = (0, -1)

vis = set()
ct = 0

while 0 < x < w-1 and 0 < y < h-1:
    xn, yn = step(x, y, d)
    vis.add((x, y, d))

    if mp[yn][xn] == '#':
        d = turn(d)

    else:
        if mp[yn][xn] == '.':
            ct += navigate(x, y, turn(d), (xn, yn))

        mp[y][x] = 'X'
        x, y = step(x, y, d)
print(ct)
