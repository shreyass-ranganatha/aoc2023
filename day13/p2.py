import re

nps = []

with open("inputs/day13.txt") as fp:
    ls = [l.strip() for l in fp.readlines() if l.strip()]

    for i in range(0, len(ls), 3):
        (xa, ya), = re.findall(r"Button A: X\+(\d+), Y\+(\d+)", ls[i])
        (xb, yb), = re.findall(r"Button B: X\+(\d+), Y\+(\d+)", ls[i+1])
        (xr, yr), = re.findall(r"Prize: X=(\d+), Y=(\d+)", ls[i+2])

        nps.append((
            int(xa), int(ya),
            int(xb), int(yb),
            int(xr) + 10000000000000, int(yr) + 10000000000000))

sm = 0

for xa, ya, xb, yb, xr, yr in nps:
    d = xa * yb - xb * ya
    x = xr * yb - xb * yr
    y = xa * yr - xr * ya

    if (x % d == 0) and (y % d == 0):
        sm += x // d * 3 + y // d
print(sm)
