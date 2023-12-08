import re

ls = []
with open("inputs/day08.txt") as f:
    for l in f:
        if l.strip():
            ls.append(l.strip())

lr = ls[0]

mp = {}
for ln in ls[1:]:
    c, l, r = re.match(r"(\w+) = \((\w+), (\w+)\)", ln).groups()
    mp[c] = (l, r)

i = 0
k = 'AAA'
while 1:
    d = lr[i % len(lr)]

    k = mp[k]['LR'.index(d)]
    if k == 'ZZZ':
        break

    i += 1

print(i+1)
