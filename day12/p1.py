import re

path = "inputs/day12.txt"

ls = []
with open(path) as f:
    for l in f:
        ls.append(l.strip().split())
        ls[-1][1] = [int(_) for _ in ls[-1][1].split(',')]

def search(st, pt, ks=[]):
    k = st.find('?')
    if k < 0:
        zt = re.findall(r"#+", st)
        if [len(_) for _ in zt] == pt:
            ks.append(st)
        return

    search(st[:k] + '.' + st[k+1:], pt)
    search(st[:k] + '#' + st[k+1:], pt)

    return ks

for i, l in enumerate(ls):
    print(i)

    zs = search(*l)
print(len(zs))
