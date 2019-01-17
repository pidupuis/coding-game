const [N, L, E] = readline().split(' ').map(Number);

const graph = [...Array(N)].map(() => []);
const gates = [...Array(E)].map(() => []);

for (let i = 0; i < L; i++) {
    const [N1, N2] = readline().split(' ').map(Number);
    graph[N1].push(N2);
    graph[N2].push(N1);
}

for (let i = 0; i < E; i++) {
    gates[i] = + readline();
}

while (true) {
    const SI = + readline();
    let C1;
    let C2 = SI;

    // First case: agent close to gate
    const neighbours = graph[SI];
    const gate = neighbours.find(n => gates.indexOf(n) !== -1);

    if (gate !== undefined) {
        C1 = gate;
    } else if (neighbours.length === 2) {
        // Second case: agent has two options, cut the one with more neighbours
        if (graph[neighbours[0]].length < graph[neighbours[1]].length) {
            C1 = neighbours[1];
        } else {
            C1 = neighbours[0];
        }
    } else {
        // Third case: cut a gate neighbour having 3 neighbours itself
        const gateNeighbours = [];
        for (let g in gates) {
            const gn = graph[g];

            for (let n = 0; n < gn.length; n++) {
                if (graph[gn[n]].length === 3) {
                    gateNeighbours.push(gn[n]);
                }
            }
        }
        C1 = gateNeighbours[0];
        C2 = graph[C1].find(n => gateNeighbours.indexOf(n) !== -1);

        if (C2 === undefined) {
            // Fourth case: cut a random agent neighbour
            C1 = neighbours[0];
            C2 = SI;
        }
    }

    graph[C1] = graph[C1].filter(x => x !== C2);
    graph[C2] = graph[C2].filter(x => x !== C1);

    print(C1, C2);
}
