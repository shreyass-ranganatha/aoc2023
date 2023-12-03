import re
import functools


@functools.cache
def is_special(a, b):
    try:
        return re.match(r"[^a-zA-Z0-9.]", ls[a][b]) is not None
    except IndexError:
        return False


ls = []
with open("inputs/day03.txt") as f:
    ls = [_.strip() for _ in f]

ln = len(ls[0])

sm = 0
for i, l in enumerate(ls):
    for s in re.finditer(r"\d+", l):
        p1, p2 = s.span()
        nb = s.group()

        for x in range(p1, p2):
            p = [
                (i-1, x-1), (i-1, x), (i-1, x+1),
                (i, x-1), (i, x+1),
                (i+1, x-1), (i+1, x), (i+1, x+1)
            ]

            for (a, b) in p:
                if not 0 <= a < ln or not 0 <= b < ln:
                    continue

                if is_special(a, b):
                    break
            else:
                continue
            break
        else:
            continue

        sm += int(nb)
print(sm)
