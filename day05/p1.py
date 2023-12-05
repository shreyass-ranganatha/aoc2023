from collections import defaultdict
import re

ls = []
with open("inputs/day05.txt") as f:
    for l in f:
        ls.append(l.strip())

_, seeds = ls.pop(0).split(': ')
seeds = [int(_) for _ in seeds.split()]

rng = defaultdict(list)
trs = {}

f = None
for i, l in enumerate(ls):
    mp1 = re.match(r"^(\w+)\-to\-(\w+) map", l)
    mp2 = re.match(r"(\d+) (\d+) (\d+)", l)

    if mp1:
        a, b = mp1.groups()
        trs[a] = b
        f = a

    elif mp2:
        rng[f].append([int(_) for _ in mp2.groups()])

def search(v, key):
    for d, s, r in rng[key]:
        if s <= v < s+r:
            v = d + v - s
            break

    if key != "location":
        return search(v, trs[key])
    else:
        return v


print(min(search(k, "seed") for k in seeds))
