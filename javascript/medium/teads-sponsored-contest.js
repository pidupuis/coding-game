const N = +readline();

const edges = [...Array(N)]
    .map(readline)
    .reduce((r, e, i, a) => {
        const [n1, n2] = e.split(' ');

        r[n1] = r[n1] || [];
        r[n2] = r[n2] || [];

        if (r[n1].indexOf(n2) === -1) {
            r[n1].push(n2);
        }
        if (r[n2].indexOf(n1) === -1) {
            r[n2].push(n1);
        }

        return r;
    }, {});

let counter = 0;

while(Object.keys(edges).length) {
    const leaves = Object.keys(edges).filter(e => edges[e].length < 2);
    for (l of leaves) {
        delete edges[l];
    }
    for (k in edges) {
        edges[k] = edges[k].filter(n => !leaves.includes(n));
        if (!edges[k].length) {
            delete edges[k];
        }
    }
    counter++;
}

print(counter);
