

ls = []
with open("inputs/day04.txt") as f:
    for ln in f:
        ls.append(ln.strip())

sm = 0

for ln in ls:
    nb, cards = ln.split(':')

    cw, cy = cards.strip().split('|')
    cw = {int(_) for _ in cw.strip().split()}
    cy = {int(_) for _ in cy.strip().split()}

    # for cw in
    pw = len(cw.intersection(cy)) - 1
    sm += 2 ** pw if pw >= 0 else 0

print(sm)
