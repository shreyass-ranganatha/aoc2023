

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

C = set()

for i in range(1, sz-1):
    # LEFT / RIGHT
    mxL, mxR = dt[i][0], dt[i][-1]
    mxT, mxB = dt[0][i], dt[-1][i]

    for j in range(1, sz-1):
        if dt[i][j] > mxL:
            C.add((i, j))
            mxL = dt[i][j]

        if dt[i][-j-1] > mxR:
            C.add((i, sz + (-j-1)))
            mxR = dt[i][-j-1]

        if dt[j][i] > mxT:
            C.add((j, i))
            mxT = dt[j][i]

        if dt[-j-1][i] > mxB:
            C.add((sz + (-j-1), i))
            mxB = dt[-j-1][i]

print(*C, sep='\n')
print(len(C) + sz * 4 - 4)
