
ls = []
with open("inputs/day06.txt") as f:
    for l in f:
        ls.append(l.strip().split())

t = int(''.join(ls[0][1:]))
d = int(''.join(ls[1][1:]))

for a in range(t+1):
    if (t-a) * a > d:
        break

for b in range(t+1, 0, -1):
    if (t-b) * b > d:
        break

print(b - a + 1)
