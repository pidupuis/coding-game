n = int(input())
v = [int(i) for i in input().split()]

d, m = 0, v[0]
for x in v[1:]:
    d, m = max(d, m - x), max(m, x)
print(-d)
