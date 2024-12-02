
def scan(l, o):
    for i in range(len(l) - 1):
        if (o and l[i] > l[i+1]) or (not o and l[i] < l[i+1]):
            return 0

        if not 1 <= abs(l[i] - l[i+1]) <= 3:
            return 0
    return 1

with open("inputs/day02.txt") as fp:
    ls = fp.readlines()

ct = 0

for l in ls:
    l = [int(n) for n in l.strip().split()]

    for i in range(len(l) - 1):
        if not (l[i] < l[i+1] and 1 <= l[i+1] - l[i] <= 3):
            if any([
                scan(l[:i+1] + l[i+2:], 1),
                scan(l[:i] + l[i+1:], 1)
            ]):
                ct += 1

            break
    else:
        ct += 1

        continue

    for i in range(len(l) - 1):
        if not (l[i] > l[i+1] and 1 <= l[i] - l[i+1] <= 3):
            if any([
                scan(l[:i+1] + l[i+2:], 0),
                scan(l[:i] + l[i+1:], 0)
            ]):
                ct += 1

            break
    else:
        ct += 1

        continue

print(ct)
