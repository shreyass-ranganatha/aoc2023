
count = 0

with open("inputs/inp04.txt") as fp:
    rw = fp.readlines()

for ln in rw:
    x, y = ln.strip().split(',')

    a, b = map(int, x.split('-'))
    c, d = map(int, y.split('-'))


    if c <= a <= b <= d or a <= c <= d <= b:
        count += 1

print(count)
