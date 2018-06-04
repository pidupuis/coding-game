readline();

closest = readline()
    .split(' ')
    .sort((a, b) => Math.abs(a) - Math.abs(b) || b - a);

print(closest[0] || 0);
