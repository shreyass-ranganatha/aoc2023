
def next(x, y, mv):
    xn, yn = x, y

    match mv:
        case ">":
            xn += 1
        case "<":
            xn -= 1
        case "^":
            yn -= 1
        case "v":
            yn += 1

    return xn, yn

def move(x, y, mv):
    xn, yn = next(x, y, mv)

    if mp[yn][xn] == "#" or not (0 <= xn < w and 0 <= yn < h):
        return

    elif mp[yn][xn] == ".":
        mp[yn][xn], mp[y][x] = mp[y][x], mp[yn][xn]

    elif mp[yn][xn] == "O":
        if not move(xn, yn, mv):
            return

        mp[yn][xn], mp[y][x] = mp[y][x], mp[yn][xn]
    return xn, yn

with open("inputs/day15.txt") as fp:
    x = y = None
    mp = []

    for j, l in enumerate(fp):
        l = l.strip()
        if not l:
            break

        if '@' in l:
            x, y = l.index('@'), j
        mp.append([*l])

    moves = ""

    for l in fp:
        l = l.strip()
        if not l:
            break

        moves += l

h, w = len(mp), len(mp[0])

for mv in moves:
    if (p := move(x, y, mv)) is not None:
        x, y = p

sm = 0
for j, l in enumerate(mp):
    for i, c in enumerate(l):
        if c == "O":
            sm += j * 100 + i

print(sm)
