l = int(input())
h = int(input())
t = input()
for i in range(h):
    row = input()
    answer = ""
    for c in t:
        pos = ord(c.lower()) - 97
        pos = pos if pos >= 0 and pos <= 25 else 26
        answer += row[pos * l:(pos + 1) * l]
    print(answer)
