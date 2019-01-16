const speed = + readline();
const N = + readline();

lights = [...Array(N)].map(() => readline().split(' '));

for (let s = speed; s > 0; s--) {
    let working = true;
    for (let i = 0; i < N; i++) {
        const [distance, duration] = lights[i];
        timeToReach = Math.round(distance / (s / 3.6));
        working = working && (Math.floor(timeToReach / duration) % 2 === 0);
    }
    if (working) {
        print(s);
        break;
    }
}
