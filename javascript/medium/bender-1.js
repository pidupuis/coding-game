// Get grid
const [R, C] = readline().split(' ').map(Number);
let grid = [...Array(R)]
    .map(() => readline().split(''));

// Get directions
const directions = {
    // direction: [x, y]
    'SOUTH': [0, 1],
    'EAST': [1, 0],
    'NORTH': [0, -1],
    'WEST': [-1, 0]
};

// Get start pos
const start = grid.flat().findIndex(c => c === '@');

// Get teleporters if any
const teleporters = grid.flat().reduce((a, e, i) => {
    if (e === 'T') {
        a.push(i);
    }
    return a;
}, []);

// Create bot
let bot = {
    priorities: ['SOUTH', 'EAST', 'NORTH', 'WEST'],
    currentDirection: 'SOUTH',
    x: start % C,
    y: Math.floor(start / C),
    path: [],
    traces: [],
    breaker: false,
    inverted: false,
}

let loop = false;
while(true) {
    let end = false;
    
    // Check current cell
    const current = grid[bot.y][bot.x];
    switch (current) {
        case 'S':
            bot.currentDirection = 'SOUTH';
            break;
        case 'E':
            bot.currentDirection = 'EAST';
            break;
        case 'N':
            bot.currentDirection = 'NORTH';
            break;
        case 'W':
            bot.currentDirection = 'WEST';
            break;
        case 'I':
            bot.priorities = bot.priorities.reverse();
            bot.inverted = !bot.inverted;
            break;
        case 'B':
            bot.breaker = !bot.breaker;
            break;
        case 'T':
            const posT = bot.y * C + bot.x;
            const otherT = teleporters.filter(t => t !== posT);
            bot.x = otherT % C;
            bot.y = Math.floor(otherT / C);
            break;
        case '$':
            end = true;
            break;
    }
    
    // Check for loop
    if (bot.traces.filter(t => t === 'x' + bot.x + 'y' + bot.y + (bot.breaker ? 'b' : '') + (bot.inverted ? 'i' : '')).length > 5) {
        loop = true;
        break;
    }
    
    // Check for end
    if (end) {
        break;
    }

    // Check where to go
    let moved = false;
    let tried = 0;
    while(!moved && tried < 4) {
        let d = bot.currentDirection;
        let nextVal = grid[bot.y + directions[d][1]][bot.x + directions[d][0]];
        
        let mapChanged = false;
        if (bot.breaker && nextVal === 'X') {
            grid[bot.y + directions[d][1]][bot.x + directions[d][0]] = ' ';
            nextVal = ' ';
            mapChanged = true;
        }
    
        if ([' ', 'S', 'E', 'N', 'W', 'I', 'B', 'T', '@', '$'].includes(nextVal)) {
            bot.path.push(d);
            bot.x += directions[d][0];
            bot.y += directions[d][1];
            bot.traces.push('x' + bot.x + 'y' + bot.y + (bot.breaker ? 'b' : '') + (bot.inverted ? 'i' : ''));
            moved = true;
        } else if (['X', '#'].includes(nextVal)) {
            bot.currentDirection = bot.priorities[tried];
            tried += 1;
        }

        if (mapChanged) {
            bot.traces = [];
        }
    }
}

print(loop ? 'LOOP' : bot.path.join('\n'));
