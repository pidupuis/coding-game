graphs = {}
for _ in range(int(input())):
    x, y = map(int, input().split())
    graphs[x] = graphs.get(x, []) + [y]

def path_length(n):
    cpt = 0
    for c in graphs.get(n, []):
        cpt = max(cpt, path_length(c))
    return 1 + cpt

longest = 0
for n in graphs:
    longest = max(longest, path_length(n))
print(longest)
