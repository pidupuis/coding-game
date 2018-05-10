import math

def co(i):
    return float(i.replace(",", "."))
    
def distance(a, b):
    x = (a[0] - b[0]) * math.cos((a[1] + b[1]) / 2)
    y = a[1] - b[1]
    return math.sqrt(x**2 + y**2) * 6371
    
u = (co(input()), co(input()))
addresses, distances = [], []

for _ in range(int(input())):
    defib = input().split(";")
    addresses.append(defib[1])
    distances.append(distance(u, (co(defib[4]), co(defib[5]))))
print(addresses[distances.index(min(distances))])
