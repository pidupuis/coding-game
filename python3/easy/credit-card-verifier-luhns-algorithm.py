for _ in range(int(input())):
    card = input().replace(" ", "")
    print(("YES", "NO")[
        int(bool((
            sum([int(card[i])*2 - 9 if int(card[i]) >= 5 else int(card[i])*2 for i in range(14, -1, -2)]) +
            sum([int(card[i]) for i in range(1, 16, 2)])
        ) % 10))
    ])
