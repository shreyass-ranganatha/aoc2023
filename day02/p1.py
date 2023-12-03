
sm = 0
with open("inputs/day02.txt") as f:
    for ln in f:
        ln = ln.strip()

        id_, sets = ln.split(':')
        sets = sets.strip().split(';')

        for s in sets:
            s = s.strip()

            for n, c in [_.strip().split() for _ in s.split(',')]:
                n = int(n)

                if c == "red" and n > 12 or c == "green" and n > 13 or c == "blue" and n > 14:
                    break
            else:
                continue
            break
        else:
            sm += int(id_.split()[1])
print(sm)

