readline();

closest = readline()
    .split(' ')
    .map((n) => + n)
    .reduce((accumulator, current) => {
        if (current < 0) {
            accumulator[0] = Math.max(accumulator[0], current);
        } else {
            accumulator[1] = Math.min(accumulator[1], current);
        }
        return accumulator;
    }, [-Infinity, Infinity]);

print(Math.abs(closest[0]) < closest[1] ? closest[0] : closest[1]);
