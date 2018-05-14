from operator import add

l, b, r = (-1, 0), (0, 1), (1, 0)
move = [
    {                                  },
    { "LEFT": b, "TOP": b, "RIGHT": b, },
    { "LEFT": r,           "RIGHT": l, },
    {            "TOP": b,             },
    {            "TOP": l, "RIGHT": b, },
    { "LEFT": b, "TOP": r,             },
    { "LEFT": r,           "RIGHT": l, },
    {            "TOP": b, "RIGHT": b, },
    { "LEFT": b,           "RIGHT": b, },
    { "LEFT": b, "TOP": b,             },
    {            "TOP": l,             },
    {            "TOP": r,             },
    {                      "RIGHT": b, },
    { "LEFT": b,                       },
]

_, h = map(int, input().split())
rooms = [list(map(int, input().split(" "))) for _ in range(h)]
_ = int(input())

while True:
    x, y, pos = input().split()
    x, y = int(x), int(y)
    next_move = move[rooms[y][x]][pos]
    print("%s %s" % tuple(map(add, (x, y), next_move)))
