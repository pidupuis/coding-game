[lx, ly, tx, ty] = readline().split(' ').map(n => parseInt(n))

while (true) {
    parseInt(readline())
    
    if (ly > ty) {
        move = "S"
        ty += 1
    }
    else if (ly < ty) {
        move = "N"
        ty -= 1
    }
    else {
        move = ""
    }

    if (lx > tx) {
        move += "E"
        tx += 1
    }
    else if (lx < tx) {
        move += "W"
        tx -= 1
    }

    print(move)
}
