n = int(input())

for i, e in enumerate(range(1, n * 2, 2)):
    print(
        "." * (i==0) +
        " " * ((n * 2) - i - 1 - (i==0)) +
        "*" * e
    )

for i, e in enumerate(range(1, n * 2, 2)):
    print(
        " " * (n - i - 1) +
        "*" * e +
        " " * ((n * 2) - e) +
        "*" * e
    )
