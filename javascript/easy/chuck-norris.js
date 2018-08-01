const binary = readline()
    .split('')
    .map((c) => ('0'.repeat(7) + c.charCodeAt(0).toString(2)).slice(-7))
    .join('');

const groups = [binary[0], '01'.replace(binary[0], '')]
    .map((n) => binary
        .split(new RegExp(n + '+'))
        .map((c) => c ? (+c ? '0 ' : '00 ') + '0'.repeat(c.length) : '')
    );

print(
    [...Array(Math.max(...groups.map((g) => g.length)))]
        .map((v, i) => [groups[0][i], groups[1][i]].join(' '))
        .join(' ')
        .trim()
);
