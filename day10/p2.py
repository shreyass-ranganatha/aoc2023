
path = 'inputs/day10.txt'

ls = []
with open(path) as f:
    for l in f:
        ls.append(l.strip())

def get_s():
    for i, l in enumerate(ls):
        if 'S' in l:
            return (i, l.index('S'))

def getnext(a, b):
    c = [a[0] - b[0], a[1] - b[1]]
    k = ls[b[0]][b[1]]

    mp = {
        '|': [[-1, 0], [1, 0]],
        'L': [[-1, 0], [0, 1]],
        '-': [[0, -1], [0, 1]],
        'J': [[0, -1], [-1, 0]],
        '7': [[1, 0], [0, -1]],
        'F': [[1, 0], [0, 1]]
    }

    try:
        r = mp[k][(1 - mp[k].index(c))]
    except (KeyError, ValueError):
        return None

    return [b[0] + r[0], b[1] + r[1]]

def getpaths(ps):
    x, y = ps

    paths = []
    for (a, b) in [
        [x-1, y-1], [x-1, y], [x-1, y+1],
        [x, y-1], [x, y+1],
        [x+1, y-1], [x+1, y], [x+1, y+1],
    ]:
        if getnext(ps, (a, b)):
            paths.append([a, b])

    return paths

x, y = get_s()
pt = getpaths((x, y))

path = [[x, y], pt[0]]

while path[-1] != path[0]:
    a, b = path[-2], path[-1]
    c = getnext(a, b)

    path.append(c)

path = path[::-1]

A = 0
for i, a in enumerate(path[:-1]):
    b = path[i+1]
    A += a[0] * b[1] - a[1] * b[0]

x = A/2 - (len(path) - 1)/2 + 1
print(x)