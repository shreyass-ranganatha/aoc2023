
with open("inputs/day09.txt") as fp:
    l = [*map(int, fp.read().strip())]

ar = []

for i, n in enumerate(l):
    if i % 2 == 0:
        ar.extend([i // 2] * n)
    else:
        ar.extend("." * n)

i = -1
j = len(ar)

while i < j:
    for i in range(i+1, j):
        if ar[i] == '.':
            break
    else:
        break

    for j in range(j-1, i, -1):
        if ar[j] != '.':
            break
    else:
        break

    ar[i], ar[j] = ar[j], ar[i]

sm = 0

for i, n in enumerate(ar):
    if n == '.':
        break

    sm += i * n
print(sm)
