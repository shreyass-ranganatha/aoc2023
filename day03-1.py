
p = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def Qpriority(ln):
    ln = ln.strip()
    a, b = ln[:len(ln)//2], ln[len(ln)//2:]

    assert len(a) == len(b)

    for c in a:
        if c not in b:
            continue

        return p.index(c) + 1


with open("inputs/inp03.txt") as fp:
    rw = fp.readlines()

sm = 0
for ln in rw:
    sm += Qpriority(ln)

print(sm)
