

S = []
P = {}

with open("inputs/inp07.txt") as fp:
    dt = [ln.strip() for ln in fp.readlines()]

for ln in dt:
    match ln.split():
        case ["$", "cd", d]:
            if d == "..":
                P['/'.join(S[:-1])] += P['/'.join(S)]
                S.pop()

            else:
                S.append(d)
                P['/'.join(S)] = 0

        case [size, p] if size.isnumeric():
            P['/'.join(S)] += int(size)

else:
    while len(S) != 1:
        P['/'.join(S[:-1])] += P['/'.join(S)]
        S.pop()

print(sum(v for k, v in P.items() if v <= 100_000))
