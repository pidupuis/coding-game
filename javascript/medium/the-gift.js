const N = +readline();
let C = +readline();

const budgets = [...Array(N)].map(readline).map(Number).sort((a, b) => a - b);

if (budgets.reduce((a, b) => a + b, 0) < C) {
    print('IMPOSSIBLE');
} else {
    print(budgets
        .reduce((r, e, i, a) => {
            const d = Math.floor((C - r.reduce((a, b) => a + b, 0)) / (a.length - r.length));
            r.push(d > e ? e : d);
            return r;
        }, [])
        .join('\n')
    );
}
