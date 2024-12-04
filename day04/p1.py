
def find_words(x, y):
    h, w = len(dt), len(dt[0])
    ds = (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)

    for dx, dy in ds:
        r = "X"

        for i in range(1, 4):
            cx, cy = x + dx * i, y + dy * i

            if 0 <= cx < h and 0 <= cy < w:
                r += dt[cx][cy]

        if r == "XMAS":
            yield 1

with open("inputs/day04.txt") as fp:
    dt = [l.strip() for l in fp.readlines()]

h, w = len(dt), len(dt[0])
sm = 0

for i in range(h):
    for j in range(w):
        if dt[i][j] == "X":
            sm += sum(find_words(i, j))
print(sm)
