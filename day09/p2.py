
with open("inputs/day09.txt") as fp:
    l = [*map(int, fp.read().strip())]

ar = []

for i, n in enumerate(l):
    if i % 2 == 0:
        ar.extend([i // 2] * n)
    else:
        ar.extend("." * n)

n = i // 2 + 1
j = len(ar)

while i < j:
    n -= 1

    for j in range(j-1, 0, -1):
        if ar[j] == n:
            break
    else:
        break

    for i in range(0, j):
        c = l[n * 2]

        if ar[i:i+c] == ['.'] * c:
            break
    else:
        continue

    ar[i:i+c], ar[j-c+1:j+1] = ar[j-c+1:j+1], ar[i:i+c]

sm = 0

for i, n in enumerate(ar):
    if n == '.':
        continue

    sm += i * n
print(sm)
