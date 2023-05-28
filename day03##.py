
p = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def Gpriority(a, b, c):
    a = a.strip()
    b = b.strip()
    c = c.strip()

    for x in a:
        if x not in b:
            continue

        if x not in c:
            continue

        return p.index(x) + 1


with open("inputs/inp03.txt") as fp:
    rw = fp.readlines()

sm = 0
for i in range(0, len(rw), 3):
    sm += Gpriority(*rw[i:i+3])

print(sm)
