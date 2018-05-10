from re import finditer

w, h = int(input()), int(input())
nodes = [(c.start(), i) for i in range(h) for c in finditer("0", input())]

for i, n in enumerate(nodes):
    n2 = [it for it in nodes[i+1:] if it[1] == n[1]]
    n3 = [it for it in nodes[i+1:] if it[0] == n[0]]
    print("{} {} {} {} {} {}".format(
        n[0],
        n[1],
        n2[0][0] if len(n2) else -1,
        n2[0][1] if len(n2) else -1,
        n3[0][0] if len(n3) else -1,
        n3[0][1] if len(n3) else -1,
    ))
