readline();
print(readline()
    .split(' ')
    .map((n) => + n)
    .reduce((accumulator, current) => {
        const posAccumulator = Math.abs(accumulator);
        const posCurrent = Math.abs(current);
        if (posCurrent === posAccumulator) {
            return posCurrent;
        } else if (posCurrent < posAccumulator) {
            return current;
        }
        return accumulator;
    }, Infinity)
);
