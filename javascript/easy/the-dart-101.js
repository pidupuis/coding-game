const N = + readline();
const players = [...Array(N)].map(readline);

print(players
    .map((name) => {
        const shoots = readline()
            .split(' ')
            .reduce((r, e) => {                
                r[name] = (r[name] || {
                    name: name,
                    dartNumber: 0,
                    roundNumber: 0,
                    score: 0,
                    roundScore: 0,
                    missed: 0,
                });
                
                if (!r[name].dartNumber || r[name].dartNumber === 3) { // if new round
                    r[name].roundNumber += 1;
                    r[name].dartNumber = 1;
                    r[name].missed = 0;
                } else {
                    r[name].dartNumber += 1;
                }
                
                if (e === 'X') {
                    r[name].missed += 1;
                    switch (r[name].missed) {
                        case 1:
                            r[name].score -= 20;
                            break;
                        case 2:
                            r[name].score -= 30;
                            break;
                        case 3:
                            r[name].score = 0;
                            break;
                    }
                    if (r[name].dartNumber === 3) {
                        r[name].roundScore = r[name].score;
                    }
                } else {
                    r[name].missed = 0;
                    let tempScore = r[name].score + eval(e);
                    if (tempScore > 101) {
                        r[name].score = r[name].roundScore;
                        r[name].dartNumber = 3; // End round
                    } else {
                        r[name].score = tempScore;
                        if (r[name].dartNumber === 3) {
                            r[name].roundScore = tempScore;
                        }
                    }
                }

                return r;
            }, {});
        return shoots[name];
    })
    .filter(p => p.score === 101)
    .sort((a, b) => a.roundNumber - b.roundNumber)
    [0].name)
