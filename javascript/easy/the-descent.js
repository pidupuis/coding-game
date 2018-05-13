while (true) {
    var mountains = [...Array(8)]
        .map(n => parseInt(readline()));
    print(mountains.indexOf(Math.max(...mountains)));
}
