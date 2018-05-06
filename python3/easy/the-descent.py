while True:
    mountains = []
    for i in range(8):
        mountains.append(int(input()))
    print(mountains.index(max(mountains)))
