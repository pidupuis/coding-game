from collections import deque

v = "234567891JQKA"
p1 = deque([v.index(input()[0]) for _ in range(int(input()))])
p2 = deque([v.index(input()[0]) for _ in range(int(input()))])

rounds = 0
while p1 and p2:
    rounds += 1
    s1 = [p1.popleft()]
    s2 = [p2.popleft()]
    while s1[-1] == s2[-1]:
        if min(len(p1), len(p2)) < 4:
            print("PAT")
            exit()
        for _ in range(4):
            s1.append(p1.popleft())
            s2.append(p2.popleft())
    winner = s1[-1] < s2[-1]
    [p1, p2][winner] += s1 + s2

print((1,2)[winner], rounds)
