n = int(input())
h = n * 2

lines = [""] * h
for i, e in enumerate(range(1, h, 2)):
    lines[i] = "{}{}".format(
        " " * (h - i - 1),
        "*" * e,
    )
    lines[i + n] = "{}{}{}{}".format(
        " " * (n - i - 1),
        "*" * e,
        " " * (h - e),
        "*" * e,
    )

lines[0] = ".{}".format(lines[0][1:])
print("\n".join(lines))
