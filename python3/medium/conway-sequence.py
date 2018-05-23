from itertools import groupby

r = input().split()
for _ in range(int(input())-1):
    t, r = r, []
    for k, g in groupby(t):
        r += [str(len(list(g))), k]
print(" ".join(r))
