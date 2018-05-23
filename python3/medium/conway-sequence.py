from itertools import groupby

def next_row(row):
    for v, g in groupby(row):
        yield from (sum(1 for _ in g), v)

r = [int(input())]
for _ in range(int(input())-1):
    r = next_row(r)
print(*r)
