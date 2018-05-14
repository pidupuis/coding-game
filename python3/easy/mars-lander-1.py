_ = [input() for _ in range(int(input()))]

while True:
    _, y, _, v, *_ = map(int, input().split())        
    print(0, 4 - int(y / (sum(range(2, abs(v))) or 1)) % 4)
