from collections import defaultdict

def is_ordered(l):
    ds = set()

    for n in l:
        if n in ds:
            return 0
        ds.update(gt[n])
    return 1

def reorder(l):
    r = [l.pop(0)]

    while l:
        n = l.pop()

        for i in range(len(r)):
            if r[i] in lt[n]:
                r.insert(i, n)
                break
        else:
            r.append(n)
    return r

po = []
pn = []

with open("inputs/day05.txt") as fp:
    while (ln := fp.readline().strip()):
        po.append([*map(int, ln.split('|'))])

    while (ln := fp.readline().strip()):
        pn.append([*map(int, ln.split(','))])

lt = defaultdict(set)
gt = defaultdict(set)
for a, b in po:
    lt[a].add(b)
    gt[b].add(a)

sm = 0

for l in pn:
    if is_ordered(l):
        continue

    l = reorder(l)
    sm += l[len(l) // 2]

print(sm)
