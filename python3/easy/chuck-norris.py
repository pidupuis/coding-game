import sys
from itertools import groupby

seq = "".join(format(ord(x), "b").zfill(7) for x in input())

answer = ""
for k, g in groupby(seq):
    answer += "{} {} ".format(("00", "0")[int(k)], "0" * len(list(g)))
print(answer.strip())
