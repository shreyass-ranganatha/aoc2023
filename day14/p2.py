import re

nps = []
h = w = 0

with open("inputs/day14.txt") as fp:
    for l in fp:
        (px, py, vx, vy), = re.findall(
            r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)",
            l.strip())

        h = max(h, int(py))
        w = max(w, int(px))

        nps.append([int(px), int(py), int(vx), int(vy)])

step = 0

with open("drawings.txt", 'w') as wf:
    for j in range(10000):
        mp = [[" "] * (w + 1) for _ in range(h + 1)]

        for i, (px, py, vx, vy) in enumerate(nps):
            y = (py + vy) % (h + 1)
            x = (px + vx) % (w + 1)

            mp[y][x] = "#"

            nps[i][0] = x
            nps[i][1] = y

        step += 1

        wf.write("\n".join("".join(r) for r in mp) + "\n")
        wf.write(f"\nstep: {step}\n\n" + "-" * 75 + "\n")
