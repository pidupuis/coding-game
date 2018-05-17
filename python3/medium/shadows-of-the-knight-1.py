w, h = map(int, input().split())
n = int(input())
x, y = map(int, input().split())
gx1, gx2, gy1, gy2 = 0, w - 1, 0, h - 1

while True:
    d = input()
    if "R" in d:
        gx1 = x + 1
    if "L" in d:
        gx2 = x - 1
    if "D" in d:
        gy1 = y + 1
    if "U" in d:
        gy2 = y - 1

    x = (gx1 + gx2) // 2
    y = (gy1 + gy2) // 2
    print(x, y)
