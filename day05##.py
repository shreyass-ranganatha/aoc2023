
import re


def lget(ar, i):
    try:
        return ar[i]
    except IndexError:
        return '   '

with open("inputs/inp05.txt") as fp:
    rw = iter(fp.readlines())

rst = []
for ln in rw:
    ln = ln.rstrip()
    if not ln:
        break

    rst.append([])
    for i in range(0, len(ln), 4):
        rst[-1].append(ln[i:i+3])

stacks = {
    int(k.strip()): [l[i] for l in rst[-2::-1] if (i := int(k.strip()) - 1) < len(l) and l[i] != '   '] for k in rst[-1]
}

for ln in rw:
    n, a, b = re.findall(r"move (\d+) from (\d+) to (\d+)", ln.strip())[0]

    n = int(n)
    a = int(a)
    b = int(b)

    stacks[b].extend(stacks[a][-n:])
    stacks[a] = stacks[a][:-n]

# print(*stacks.items(), sep='\n')
print(*(stacks[k][-1][1] for k in stacks), sep='')
