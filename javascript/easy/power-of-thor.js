[lx, ly, tx, ty] = readline().split(' ').map(n => + n);

while (true) {
    + readline();
    
    var move = '';
    if (ly > ty) {
        move = 'S';
        ty++;
    } else if (ly < ty) {
        move = 'N';
        ty--;
    }

    if (lx > tx) {
        move += 'E';
        tx++;
    } else if (lx < tx) {
        move += 'W';
        tx--;
    }
    print(move);
}
