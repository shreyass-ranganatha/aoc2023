from collections import defaultdict
import re

ls = []
with open("inputs/day05.txt") as f:
    for l in f:
        ls.append(l.strip())

_, seeds = ls.pop(0).split(': ')
seeds = re.findall(r"\d+ \d+", seeds)

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


def getrngs(key):
    rs = []

    for d, s, r in sorted(rng[key], key=lambda _: _[0]):
        rs.append([s, s+r, d, d+r])
    return sorted(rs, key=lambda _: _[0])

def a_to_c(m1, m2):
    rm = []

    for (s11, s12, d11, d12) in m1:
        rs = []

        for (s21, s22, d21, d22) in m2:
            if d11 < s22 and d12 > s21:
                rs.append([
                    s11 + (s21 - d11) if d11 < s21 else s11,
                    s12 - (d12 - s22) if d12 > s22 else s12,
                    (d21 + (d11 - s21)) if d11 > s21 else d21,
                    (d22 - (s22 - d12)) if d12 < s22 else d22,
                ])

        if rs:
            a, b, *_ = rs[0]
            rs.insert(0, [s11, a, d11, d11 + (a - d11)])
            if rs[0][0] == rs[0][1]:
                del rs[0]

            a, b, *_ = rs[-1]
            rs.append([b, s12, d12 - (s12 - b), d12])
            if rs[-1][0] == rs[-1][1]:
                del rs[-1]

        else:
            rs.append([s11, s12, d11, d12])

        rm.extend(rs)
    return rm

m1 = [[int(_) for _ in s.split()] for s in seeds]
m1 = [[a, a+b]*2 for a, b in m1]

m1 = a_to_c(m1, getrngs("seed"))
k = "seed"

while k in trs:
    k = trs[k]

    m2 = getrngs(k)
    if not m2:
        break

    m1 = a_to_c(m1, m2)

def getter(m, k):
    for a, b, c, d in m:
        if a <= k < b:
            return c + (k - a)
    return k

print(min(getter(m1, _[0]) for _ in m1))
