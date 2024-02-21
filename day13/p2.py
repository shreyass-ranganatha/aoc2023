import numpy as np


path = "da"
path = "inputs/day13.txt"

mps = [[]]

with open(path) as f:
    for ln in f:
        if not ln.strip():
            mps.append([])

        else:
            mps[-1].append( np.array(list(ln.strip())) )

mps = [np.array(_) for _ in mps if _]

def gets(mp):
    h = v = 0

    # horizontal mirror
    for i in range(1, mp.shape[0] // 2 + 1):
        if ( mp[:i, :] != mp[i:i*2, :][::-1] ).sum() == 1:
            h += i

        if ( mp[::-1][:i, :] != mp[::-1][i:i*2, :][::-1] ).sum() == 1:
            h += mp.shape[0] - i
    
    # vertical mirror
    for i in range(1, mp.shape[1] // 2 + 1):
        if ( mp[:, :i] != mp[:, i:i*2][:, ::-1] ).sum() == 1:
            v += i

        if ( mp[:, ::-1][:, :i] != mp[:, ::-1][:, i:i*2][:, ::-1] ).sum() == 1:
            v += mp.shape[1] - i

    return h, v


h = v = 0

for mp in mps:
    _h, _v = gets(mp)

    h += _h
    v += _v

print(h * 100 + v)
