
a = []
b = []

with open("inputs/day01.txt") as fp:
    for ln in fp.readlines():
        p, q = ln.split()
        a.append(int(p))
        b.append(int(q))

a = sorted(a)
b = sorted(b)

sm = 0
for p, q in zip(a, b):
    sm += abs(p - q)

print(sm)
