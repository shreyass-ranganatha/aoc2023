

with open("inputs/inp08.txt") as fp:
    dt = [list(map(int, ln.strip())) for ln in fp.read().splitlines()]

dt = [
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
]

sz = len(dt)
ct = 0

C = {}

for i in range(1, sz-1):
    # LEFT / RIGHT
    mxL, mxR = dt[i][0], dt[i][-1]
    l, r = 1, 1

    mxT, mxB = dt[0][i], dt[-1][i]
    t, b = 1, 1

    for j in range(1, sz-1):
        if dt[i][j] > mxL:
            C[(i, j)] = l if (i, j) not in C else l * C[(i, j)]
            mxL = dt[i][j]

        if dt[i][-j-1] > mxR:
            C[(i, sz + (-j-1))] = r if (i, sz + (-j-1)) not in C else r * C[(i, sz + (-j-1))]
            mxR = dt[i][-j-1]

            print((i, sz + (-j-1)), mxR, r)

        if dt[j][i] > mxT:
            C[(j, i)] = t if (j, i) not in C else t * C[(j, i)]
            mxT = dt[j][i]

        if dt[-j-1][i] > mxB:
            C[(sz + (-j-1), i)] = b if (sz + (-j-1), i) not in C else b * C[(sz + (-j-1), i)]
            mxB = dt[-j-1][i]

        l += 1
        r += 1
        t += 1
        b += 1

print(*C.items(), sep='\n')
# print(len(C) + sz * 4 - 4)
