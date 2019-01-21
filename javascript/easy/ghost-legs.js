const [W, H] = readline().split(' ').map(Number);

const labelOrder = readline().split('  ');
const labels = labelOrder
    .reduce((r, e, i) => {
        r[e] = i + 1;
        return r;
    }, {});

for (let i = 1; i < H - 1; i++) {
    const level = '  ' + readline() + '  ';
    for (let label in labels) {
        const pos = (labels[label] * 3) - 1;
        if (level[pos - 1] === '-') {
            labels[label] -= 1;
        }
        if (level[pos + 1] === '-') {
            labels[label] += 1;
        }
    }
}

const result = readline().split('  ');
for (let label of labelOrder) {
    print(label + result[labels[label] - 1]);
}
