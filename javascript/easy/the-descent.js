while (true) {
    var mountains = [];
    for (var i = 0; i < 8; i++) {
        mountains.push(parseInt(readline()));
    }
    print(mountains.indexOf(Math.max(...mountains)));
}
