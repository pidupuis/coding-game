const [N, Q] = [+ readline(), + readline()];

const extToMt = [...Array(N)]
    .map(() => readline().split(' '))
    .reduce((r, e) => (
        Object.assign(r, JSON.parse('{"' + e[0].toLowerCase() + '":"' + e[1] + '"}'))
    ), {});

print([...Array(Q)]
    .map(() => readline().toLowerCase().split('.'))
    .map((f) => f.length > 1 ? f.slice(-1) : null)
    .map((e) => extToMt[e] || 'UNKNOWN')
    .join('\n'));
