# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?
import math


def build_pascal(depth):
    if depth == 1:
        return [1]
    last_pascal = build_pascal(depth-1)
    current_pascal = [1]
    for i in range(len(last_pascal) - 1):
        current_pascal.append(last_pascal[i] + last_pascal[i+1])
    current_pascal.append(1)
    print(current_pascal)
    return current_pascal


pascal = build_pascal(20*2 + 1)
print(pascal[math.floor(len(pascal)/2)])
