x1, y1, x2, y2, _ = [0, 0] + [*map(int, input().split())] + [input()]
x, y = map(int, input().split())

while True:
    d = input()
    if "R" in d:
        x1 = x + 1
    elif "L" in d:
        x2 = x - 1
    if "D" in d:
        y1 = y + 1
    elif "U" in d:
        y2 = y - 1

    x = (x1 + x2) // 2
    y = (y1 + y2) // 2
    print(x, y)
