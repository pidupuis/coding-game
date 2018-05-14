from operator import add

move = [
    {                                                    },
    { "LEFT": ( 0, 1), "TOP": ( 0, 1), "RIGHT": ( 0, 1), },
    { "LEFT": ( 1, 0),                 "RIGHT": (-1, 0), },
    {                  "TOP": ( 0, 1),                   },
    {                  "TOP": (-1, 0), "RIGHT": ( 0, 1), },
    { "LEFT": ( 0, 1), "TOP": ( 1, 0),                   },
    { "LEFT": ( 1, 0),                 "RIGHT": (-1, 0), },
    {                  "TOP": ( 0, 1), "RIGHT": ( 0, 1), },
    { "LEFT": ( 0, 1),                 "RIGHT": ( 0, 1), },
    { "LEFT": ( 0, 1), "TOP": ( 0, 1),                   },
    {                  "TOP": (-1, 0),                   },
    {                  "TOP": ( 1, 0),                   },
    {                                  "RIGHT": ( 0, 1), },
    { "LEFT": ( 0, 1),                                   },
]

_, h = map(int, input().split())
rooms = [list(map(int, input().split(" "))) for _ in range(h)]
_ = int(input())

while True:
    x, y, pos = input().split()
    x, y = map(int, [x, y])
    print("%s %s" % tuple(map(add, (x, y), move[rooms[y][x]][pos])))
