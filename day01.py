

C = [0]

with open("inputs/inp01.txt") as fp:
    for ln in fp:
        try:
            C[-1] += int(ln.strip())
        except ValueError:
            C.append(0)

print(sum(sorted(C)[-3:]))
