import functools

@functools.cache
def possible(pt):
    if pt == '':
        return 1

    for t in tw:
        if pt.startswith(t) and possible(pt[len(t):]):
            return 1
    return 0

with open("inputs/day19.txt") as fp:
    tw = fp.readline().strip().split(', ')
    fp.readline()

    np = []
    for l in fp:
        np.append(l.strip())

sm = 0
for n in np:
    sm += possible(n)

print(sm)
