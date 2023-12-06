
ls = []
with open("inputs/day06.txt") as f:
    for l in f:
        ls.append(l.strip().split())

r = 1
for t, d in list(zip(*ls))[1:]:
    t = int(t)
    d = int(d)

    c = 0
    f = 0

    for i in range(t+1):
        if f := ((t-i) * i > d):
            c += 1
        elif f:
            break
    r *= c
print(r)
