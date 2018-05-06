import sys
import math

n = int(input())
numbers = input().split()
if not numbers:
    print(0)
else:
    pos = min([int(i) if int(i) >= 0 else math.inf for i in numbers])
    neg = max([int(i) if int(i) < 0 else (math.inf * -1) for i in numbers])
    print(pos if pos <= abs(neg) else neg)
