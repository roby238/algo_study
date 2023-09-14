import sys
import math
def solution():
    read = sys.stdin.readline
    g = int(read())
    weight = []
    for i in range(int(math.sqrt(g)), 1, -1):
        if not (g % i) and i**2 != g and not((i + g // i) % 2):
            weight.append((i + g // i) // 2)
    if g > 1 and g % 2:
        weight.append((g + 1) // 2)
    if weight:
        for w in weight:
            print(w)
    else:
        print("-1")

solution()