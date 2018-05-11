_, _, _, exit_floor, exit_pos, _, _, n = [int(i) for i in input().split()]
elevators = {int(j[0]): int(j[1]) for j in [input().split() for _ in range(n)]}
elevators[exit_floor] = exit_pos

while True:
    line = input().split()
    clone_floor, clone_pos, direction = int(line[0]), int(line[1]), line[2]
    if clone_floor < 0:
        print("WAIT")
    elif clone_pos > elevators[clone_floor] and direction == "RIGHT":
        print("BLOCK")
    elif clone_pos < elevators[clone_floor] and direction == "LEFT":
        print("BLOCK")
    else:
        print("WAIT")
