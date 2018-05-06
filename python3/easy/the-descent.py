import sys
import math

while True:
    mountains = []
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        mountains.append(mountain_h)

    # The index of the mountain to fire on.
    print(mountains.index(max(mountains)))
