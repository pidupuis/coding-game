[N, Q] = [parseInt(readline()), parseInt(readline())];

var extToMt = [...Array(N)]
    .map(n => readline())
    .reduce((r, e) => {
        r[e.split(' ')[0].toLowerCase()] = e.split(' ')[1];
        return r;
    }, {});

[...Array(Q)]
    .map(n => readline())
    .map((e) => {
        var ext = e.indexOf('.') !== -1 ? e.split('.').slice(-1).pop().toLowerCase() : null;
        print(ext in extToMt ? extToMt[ext] : 'UNKNOWN');
    });
