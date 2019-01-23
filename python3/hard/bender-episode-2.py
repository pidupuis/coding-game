rooms = {
    r: (int(m), d1, d2) for r, m, d1, d2 in (
        input().split() for i in range(int(input()))
    )
}

def explore(room, previous={'E': 0}):
    if room not in previous:
        m, d1, d2 = rooms[room]
        previous[room] = m + max(explore(d1), explore(d2))
    return previous[room]

print(explore('0'))
