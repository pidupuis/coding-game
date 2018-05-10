from math import cos, sqrt, inf

def conv(i):
    return float(i.replace(",", "."))
    
def distance(a, b):
    x = (a[0] - b[0]) * cos((a[1] + b[1]) / 2)
    y = a[1] - b[1]
    return sqrt(x**2 + y**2) * 6371
    
user = (conv(input()), conv(input()))
closest = inf, ""

for _ in range(int(input())):
    _, name, _, _, lon, lat = input().split(";")
    closest = min(closest, (distance(user, (conv(lon), conv(lat))), name))
print(closest[1])
