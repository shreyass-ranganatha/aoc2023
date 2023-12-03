

opp = ['A', 'B', 'C']
yur = ['X', 'Y', 'Z']

tscore = 0

with open("inputs/inp02.txt") as fp:
    for ln in fp:
        o, m = ln.strip().split()
        s = yur.index(m) * 3

        if m == 'X':
            s += (opp.index(o) - 1) % 3 + 1
        elif m == 'Y':
            s += opp.index(o) + 1
        elif m == 'Z':
            s += (opp.index(o) + 1) % 3 + 1

        tscore += s

print(tscore)
