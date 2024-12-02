
with open("inputs/day02.txt") as fp:
    ls = fp.readlines()

ct = 0

for l in ls:
    l = [int(n) for n in l.strip().split()]
    o = l[0] < l[1]

    for i in range(len(l) - 1):
        if (o and l[i] > l[i+1]) or (not o and l[i] < l[i+1]):
            break

        if not 1 <= abs(l[i] - l[i+1]) <= 3:
            break
    else:
        ct += 1

print(ct)
