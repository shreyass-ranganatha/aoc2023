import functools

path = "inputs/day12.txt"

ls = []
with open(path) as f:
    for l in f:
        st, pt = l.strip().split()

        ls.append((
            '?'.join([st] * 5),
            tuple(int(_) for _ in pt.split(',')) * 5
        ))

        # ls.append((st, tuple(int(_) for _ in pt.split(',')) ))

def fit(l, ls):
    if '.' in ls[:l] or (l < len(ls) and ls[l] == '#') or l > len(ls):
        return 0
    return 1

@functools.lru_cache
def gets(st, pt):
    if not st:
        return 1 if not pt else 0

    if not pt:
        return 1 if '#' not in st else 0

    r = 0
    if st[0] in '.?':
        r += gets(st[1:], pt)

    if st[0] in '#?' and fit(pt[0], st):
        r += gets(st[pt[0] + 1:], pt[1:])

    return r

sm = 0
for i, l in enumerate(ls[:]):
    k = gets(*l)
    sm += k

print(sm)
