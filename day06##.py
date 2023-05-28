
with open("inputs/inp06.txt") as fp:
    dt = fp.read()

for i in range(len(dt)):
    if len(set(dt[i-13:i+1])) == 14:
        print(i+1)
        break
