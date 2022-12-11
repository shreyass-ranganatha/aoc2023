

opp = ['A', 'B', 'C']
yur = ['X', 'Y', 'Z']

tscore = 0

with open("inputs/inp02.txt") as fp:
    for ln in fp:
        o, m = ln.strip().split()
        s = yur.index(m) + 1

        if opp.index(o) == (yur.index(m) - 1) % 3:
            s += 6
        elif opp.index(o) == yur.index(m):
            s += 3

        tscore += s

print(tscore)
