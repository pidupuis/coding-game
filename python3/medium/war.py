def round(a, b):
    v = "234567891JQKA"
    if v.index(a) == v.index(b):
        return None
    return v.index(a) > v.index(b)

p1 = [list(input())[0] for _ in range(int(input()))]
p2 = [list(input())[0] for _ in range(int(input()))]

i = 0
match = ""
war1, war2 = [], []
while True:
    l = min(len(p1), len(p2))
    if l == 0:
        print(1 if len(p1) else 2, i)
        break
    a, b = p1[0], p2[0]
    p1, p2 = p1[1:], p2[1:]
    r = round(a, b)
    if r is not None:
        cards = war1 + [a] + war2 + [b]
        if r:
            p1 += cards
            match += "1"
        else:
            p2 += cards
            match += "2"
        war1, war2 = [], []
        i += 1
    else:
        war1 += [a] + p1[:3]
        p1 = p1[3:]
        war2 += [b] + p2[:3]
        p2 = p2[3:]
        match += "W"
        if min(len(war1), len(war2)) < 4:
            print("PAT")
            break
