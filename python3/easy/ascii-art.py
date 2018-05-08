l, h = [int(input()), int(input())]
t = [ord(c.lower()) - 97 if c.isalpha() else 26 for c in input()]

for _ in range(h):
    row = input()
    print("".join(row[j * l:(j + 1) * l] for j in t))
