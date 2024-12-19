
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

def prop(x, y, mv):
    xn, yn = next(x, y, mv)

    if mp[yn][xn] == '#' or not (0 <= xn < w and 0 <= yn < h):
        return 0

    elif mp[yn][xn] == '.':
        return 1

    elif mp[yn][xn] in '[]':
        if mv in '><':
            return prop(xn, yn, mv)
        else:
            return prop(xn, yn, mv) and prop(xn + (-1 if mp[yn][xn] == ']' else 1), yn, mv)

def move(x, y, mv):
    xn, yn = next(x, y, mv)

    if mp[yn][xn] == '.':
        mp[yn][xn], mp[y][x] = mp[y][x], mp[yn][xn]

    elif mp[yn][xn] in '[]':
        if mv in '><':
            move(xn, yn, mv)
        else:
            move(xn + (-1 if mp[yn][xn] == ']' else 1), yn, mv)
            move(xn, yn, mv)

        mp[yn][xn], mp[y][x] = mp[y][x], mp[yn][xn]
    return xn, yn

with open("inputs/day15.txt") as fp:
    x = y = None
    mp = []

    for j, l in enumerate(fp):
        l = l.strip()
        if not l:
            break

        rw = []
        p2 = {
            ".": [*".."],
            "#": [*"##"],
            "O": [*"[]"],
            "@": [*"@."],
        }

        for i, c in enumerate(l):
            rw.extend(p2[c])

            if c == '@':
                x, y = i * 2, j
        mp.append(rw)

    moves = ""

    for l in fp:
        moves += l.strip()

h, w = len(mp), len(mp[0])

for mv in moves:
    if prop(x, y, mv):
        x, y = move(x, y, mv)

sm = 0
for j, l in enumerate(mp):
    for i, c in enumerate(l):
        if c == "[":
            sm += j * 100 + i

print(sm)

