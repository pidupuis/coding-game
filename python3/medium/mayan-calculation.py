import re

def get_powers(n):
    powers = []
    for i in reversed(range(15)):
        v = 20**i
        if v <= n:
            powers.append(n//v)
            n %= v
        elif len(powers):
            powers.append(0)
    return powers

def get_number(width):
    char_number = int(input())//width
    words = ["".join([input() for _ in range(width)]) for _ in range(char_number)]
    res = 0
    for i, w in enumerate(words):
        res += sum([k for k,v in dic.items() if v == w]) * 20**(char_number-i-1)
    return res


l, h = map(int, input().split())
dic = {k: "" for k in range(20)}
for i in range(h):
    for k,v in enumerate(re.findall(l*".", input())):
        dic[k] += v
n1 = get_number(l)
n2 = get_number(l)
result = eval("{}{}{}".format(n1, input(), n2))
result = [dic[r] for r in get_powers(result)] if result else dic[result]
print("\n".join(re.findall(l*".", "".join(result))))
