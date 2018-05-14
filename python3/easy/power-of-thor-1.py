lx, ly, tx, ty = [int(i) for i in input().split()]

while True:
    _ = int(input())

    move = ""
    if ly > ty:
        move = "S"
        ty += 1
    elif ly < ty:
        move = "N"
        ty -= 1

    if lx > tx:
        move += "E"
        tx += 1
    elif lx < tx:
        move += "W"
        tx -= 1
    print(move)
