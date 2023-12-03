
sm = 0
with open("inputs/day02.txt") as f:
# with open("da") as f:
    for ln in f:
        ln = ln.strip()

        id_, sets = ln.split(':')
        sets = sets.strip().split(';')

        dt = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for s in sets:
            s = s.strip()

            for n, c in [_.strip().split() for _ in s.split(',')]:
                dt[c] = max(dt[c], int(n))

        sm += dt["red"] * dt["green"] * dt["blue"]
print(sm)

