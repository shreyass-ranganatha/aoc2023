import math

path = 'inputs/day09.txt'

ls = []
with open(path) as f:
    for l in f:
        ls.append([int(_) for _ in l.strip().split()])

sm = 0
for ln in ls:
    ds = [ln.copy()]
    while not all(map(lambda _: not _, ds[-1])):
        d = []
        for i, v in enumerate(ds[-1][:-1]):
            d.append(ds[-1][i+1] - v)

        ds.append(d)

    ks = [_[0] for _ in ds]
    cb = [math.comb(len(ln), i) for i in range(len(ln)+1)]

    rs = 0
    for i, v in enumerate(ks):
        rs += v * cb[i]

    sm += rs
print(sm)
