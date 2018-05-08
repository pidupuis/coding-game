l, h, t = [int(input()), int(input()), input()]

for i in range(h):
    row = input()
    answer = ""
    for c in t:
        pos = ord(c.lower()) - 97 if c.isalpha() else 26
        answer += row[pos * l:(pos + 1) * l]
    print(answer)
