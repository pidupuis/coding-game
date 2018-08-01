const [L, H] = [+ readline(), + readline()];

const T = [...readline()]
    .map((c) => {
        if (c.toLowerCase() == c.toUpperCase()) {
            return 26;
        }
        return c.toLowerCase().charCodeAt() - 97;
    });

print([...Array(H)]
    .map(() => readline())
    .map((row) => T.map((j) => row.slice(j * L, (j + 1) * L)).join(''))
    .join('\n'));
