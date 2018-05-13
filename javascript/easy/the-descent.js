while (true) {
    const mountains = [...Array(8)]
        .map(() => + readline());
    print(mountains.indexOf(Math.max(...mountains)));
}
