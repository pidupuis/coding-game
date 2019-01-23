const N = +readline();
const rooms = [...Array(N)]
    .reduce((r, e, i, a) => {
        const [id, money, door1, door2] = readline().split(' ');
        r[i] = {
            id: +id,
            money: +money,
            total: 0,
            next: [
                (door1 === 'E') ? N : +door1,
                (door2 === 'E') ? N : +door2
            ],
        };
        return r;
    }, {});
rooms[N] = {id: N, money: 0, total: 0, next: []};

const roomsToExplore = [0];
const explore = (room, door) => {
    if (rooms[room].money + rooms[room].total > rooms[rooms[room].next[door]].total) {
        roomsToExplore.push(rooms[room].next[door]);
        rooms[rooms[room].next[door]].total = rooms[room].money + rooms[room].total;
    }
};

while (roomsToExplore.length > 0) {
    const id = roomsToExplore.shift();
    if (id < N) {
        explore(id, 0);
        explore(id, 1);
    }
}

print(rooms[N].total);
