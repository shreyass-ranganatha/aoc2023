
def dfs(r, vs):
    if len(vs) <= 1:
        return vs[0] == r

    a, b = vs.pop(0), vs.pop(0)

    return any([
        dfs(r, [a+b, *vs]),
        dfs(r, [a*b, *vs])
    ])

with open("inputs/day07.txt") as fp:
    dt = []

    for ln in fp:
        r, vs = ln.strip().split(":")
        dt.append([int(r), [*map(int, vs.strip().split())]])

sm = 0
for r, vs in dt:
    if dfs(r, vs.copy()):
        sm += r

print(sm)
