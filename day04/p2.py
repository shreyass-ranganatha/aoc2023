from collections import Counter

ls = []
with open("inputs/day04.txt") as f:
    for ln in f:
        ls.append(ln.strip())

c = Counter()

for ln in ls:
    nb, cards = ln.split(':')

    nm, nb = nb.split()
    nb = int(nb)

    cw, cy = cards.strip().split('|')
    cw = {int(_) for _ in cw.strip().split()}
    cy = {int(_) for _ in cy.strip().split()}

    pw = len(cw.intersection(cy))

    c[nb] += 1
    for i in range(nb+1, nb+pw+1):
        c[i] += max(c[nb], 1)

print(c.total())
