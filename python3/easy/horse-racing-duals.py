n = int(input())
h = sorted([int(input()) for _ in range(n)])
print(min([abs(h[i] - h[i + 1]) for i in range(n - 1)]))
