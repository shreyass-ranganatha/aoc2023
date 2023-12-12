import re
import itertools

path = "inputs/day11.txt"

ls = []
with open(path) as f:
    for l in f:
        ls.append(l.strip())

sp = 1000000

rws = []
for i, l in enumerate(ls):
    if not l.count('#'):
        rws.append(i)

cns = []
for i in range(len(ls[0])):
    if not [l[i] for l in ls].count('#'):
        cns.append(i)

c1 = []
for i, l in enumerate(ls):
    for m in re.finditer(r"#", l):
        j = m.start()
        c1.append((i, j))

def dist(a, b):
    x1, y1 = a
    x2, y2 = b

    return abs(x2 - x1) + abs(y2 - y1)

c2 = []
for i, j in c1:
    co = len([_ for _ in cns if _ < j])
    ro = len([_ for _ in rws if _ < i])

    c2.append((
        ro * sp + (i - ro),
        co * sp + (j - co)
    ))

sm = 0
for a, b in itertools.combinations(c2, 2):
    sm += dist(a, b)

print(sm)
