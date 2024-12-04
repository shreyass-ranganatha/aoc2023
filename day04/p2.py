
def find_words(x, y):
    h, w = len(dt), len(dt[0])

    if not (0 < x < h - 1 and 0 < y < w - 1):
        return 0

    s1 = "".join(dt[x-1+k][y-1+k] for k in range(3))
    s2 = "".join(dt[x-1+k][y+1-k] for k in range(3))

    if s1 in ("SAM", "MAS") and s2 in ("SAM", "MAS"):
        return 1
    return 0

with open("inputs/day04.txt") as fp:
    dt = [l.strip() for l in fp.readlines()]

h, w = len(dt), len(dt[0])
sm = 0

for i in range(h):
    for j in range(w):
        if dt[i][j] == "A":
            sm += find_words(i, j)
print(sm)
