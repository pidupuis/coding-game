const speed = + readline();
const N = + readline();

lights = [...Array(N)].map(() => readline().split(' '));

for (let s = speed; s > 0; s--) {
    let working = true;
    for (let i = 0; i < N; i++) {
        const distance = lights[i][0] / 1000;
        const duration = lights[i][1] / 3600;
        timeToReach = distance / s;
        numberOfCycle = Math.floor((timeToReach / duration) + 0.0001);
        isGreen = numberOfCycle % 2 === 0;
        working = working && isGreen;
        if (!working) break;
    }
    if (working) {
        print(s);
        break;
    }
}
