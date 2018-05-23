w, h = map(int, input().split())
codes = [input() for _ in range(h)]
digits = [[codes[i][w * d:][:w] for i in range(h)] for d in range(20)]

def get_number():
    n, numeral = 0, [input() for _ in range(int(input()))]
    while numeral:
        n = 20 * n + digits.index(numeral[:h])
        numeral = numeral[h:]
    return n

res = int(eval('{0}{2}{1}'.format(get_number(), get_number(), input())))
output = [] if res else digits[0]
while res:
    res, d = divmod(res, 20)
    output = digits[d] + output
print(*output, sep="\n")
