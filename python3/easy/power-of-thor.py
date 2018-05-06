lx, ly, tx, ty = [int(i) for i in input().split()]

while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    
    if ly > ty:
        move = "S"
        ty += 1
    elif ly < ty:
        move = "N"
        ty -= 1
    else:
        move = ""

    if lx > tx:
        move += "E"
        tx += 1
    elif lx < tx:
        move += "W"
        tx -= 1

    print(move)
