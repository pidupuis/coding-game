_ = int(input())

d = m = 0
for x in map(int, input().split()):
    d, m = min(d, x - m), max(m, x)
print(d)
