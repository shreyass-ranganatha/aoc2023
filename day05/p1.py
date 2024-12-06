from collections import defaultdict

po = []
pn = []

with open("inputs/day05.txt") as fp:
    while (ln := fp.readline().strip()):
        po.append([*map(int, ln.split('|'))])

    while (ln := fp.readline().strip()):
        pn.append([*map(int, ln.split(','))])

gt = defaultdict(list)
for a, b in po:
    gt[b].append(a)

sm = 0

for l in pn:
    ds = set()

    for n in l:
        if n in ds:
            break
        ds.update(gt[n])
    else:
        sm += l[len(l) // 2]

print(sm)
