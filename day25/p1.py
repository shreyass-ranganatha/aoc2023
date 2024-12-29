import itertools

locks = []
keys = []

with open("inputs/day25.txt") as fp:
    p = None
    t = 0

    for l in fp.readlines() + ['']:
        l = l.strip()

        if not l:
            if t:
                p = [*map(lambda x: x - 1, p)]
                keys.append(p)
            else:
                locks.append(p)

            p = None
            continue

        if p is None:
            t = l.startswith('.') and 1 or 0
            p = [0] * 5

            continue

        for j in range(5):
            p[j] += l[j] == '#' and 1 or 0

ct = 0

for l, k in itertools.product(locks, keys):
    for p, q in zip(k, l):
        if p + q >= 6:
            break
    else:
        ct += 1

print(ct)
