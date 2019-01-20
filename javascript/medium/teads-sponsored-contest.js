const N = +readline();

// Get list of edges for each node
const edges = [...Array(N)]
    .map(readline)
    .reduce((r, e, i, a) => {
        const [n1, n2] = e.split(' ');
        r[n1] = r[n1] || [];
        r[n2] = r[n2] || [];
        r[n1].push(n2);
        r[n2].push(n1);
        return r;
    }, {});

// Count every time we need to cut leaves
let counter = 0;
while(Object.keys(edges).length) {
    const deepCopy = JSON.parse(JSON.stringify(edges));
    for (let node in deepCopy) {
        // If a node is a leaf
        if (deepCopy[node].length < 2) {
            for (let neighbour of deepCopy[node]) {
                if (edges[neighbour]) {
                    // Remove the leaf from the list of edges of its direct neighbours
                    edges[neighbour] = edges[neighbour].filter(x => x !== node);
                    // If the direct neighbours has no remaining link, cut it
                    if (!edges[neighbour].length) {
                        delete edges[neighbour];
                    }
                }
            }
            // Finally cut the leaf
            delete edges[node];
        }
    }
    counter++;
}
print(counter);
