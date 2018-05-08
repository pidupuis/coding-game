surface_n = int(input())
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]        
    print(0, 4 - int(y / (sum(range(1, abs(v_speed) + 1)) or 1)) % 4)
