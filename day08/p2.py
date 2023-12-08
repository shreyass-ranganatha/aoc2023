import re
import math

ls = []
with open("inputs/day08.txt") as f:
    for l in f:
        ls.append(l.strip())

lr = ls[0]

mp = {}
for ln in ls[2:]:
    c, l, r = re.match(r"(\w+) = \((\w+), (\w+)\)", ln).groups()
    mp[c] = (l, r)

qu = [k for k in mp if k.endswith('A')]

def dfs(k):
    i = 0
    d = lambda i: 'LR'.index(lr[i % len(lr)])

    pt = [(k, i % len(lr))]
    while (mp[k][d(i)], (i+1) % len(lr)) not in pt:
        k = mp[k][d(i)]
        i += 1

        pt.append((k, i % len(lr)))
    pt.append((mp[k][d(i)], (i+1) % len(lr)))

    return pt

def getzs(k):
    d = dfs(k)
    print(k, len(d), d.index(d[-1]))

    zs = []
    for i, (k, _) in enumerate(d):
        if k.endswith('Z'):
            zs.append(i)
    return zs

rs = []
for k in qu:
    rs.append(getzs(k))

# to flatten
while type(rs[0]) is list:
    rs.extend(rs.pop(0))

print(math.lcm(*rs))
