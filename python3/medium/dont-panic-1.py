*_, f, p, _, _, n = [int(i) for i in input().split()]
elevators = {int(j[0]): int(j[1]) for j in [input().split() for _ in range(n)]}
elevators[f] = p

while True:
    f, p, d = input().split()
    print(("BLOCK","WAIT")["-" in f or (int(p) - int(elevators[int(f)])) * d.find("I") <= 0])
