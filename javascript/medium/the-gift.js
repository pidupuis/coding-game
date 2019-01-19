const N = +readline();
let price = +readline();

const budgets = [...Array(N)].map(() => +readline()).sort((a, b) => a - b);
const sum = budgets.reduce((a, b) => a + b, 0);

if (sum < price) {
    print('IMPOSSIBLE');
} else {
    while(budgets.length) {
        const d = Math.floor(price / budgets.length);
        const b = budgets.shift();
        const res = d > b ? b : d;
        price -= res;
        print(res);
    }
}
