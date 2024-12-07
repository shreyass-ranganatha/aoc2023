
def turn(d):
    return -d[1], d[0]

def step(x, y, d):
    dx, dy = d
    return x+dx, y+dy

with open("inputs/day06.txt") as fp:
    mp = []

    for j, l in enumerate(fp):
        l = l.strip()

        if '^' in l:
            x, y = l.index('^'), j
        mp.append([*l])

h, w = len(mp), len(mp[0])
d = (0, -1)

ct = 1 # first position

while 0 < x < w-1 and 0 < y < h-1:
    xn, yn = step(x, y, d)

    if mp[yn][xn] == '#':
        d = turn(d)

    else:
        ct += 1 if mp[y][x] != 'X' else 0
        mp[y][x] = 'X'

        x, y = step(x, y, d)
print(ct)