from collections import Counter

ct = Counter()
a = []

with open("inputs/day01.txt") as fp:
    for ln in fp.readlines():
        p, q = ln.split()
        a.append(int(p))

        ct[int(q)] += 1


print(sum([p * ct.get(p, 0) for p in a]))
