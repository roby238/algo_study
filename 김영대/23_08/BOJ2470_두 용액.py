import sys
def solution():
    read = sys.stdin.readline
    n = int(read().rstrip())
    v = list(map(int, read().rstrip().split()))

    v.sort(key = lambda x : abs(x))

    li1 = 0; li2 = 0; minSum = 2000000000
    for i in range(n):
        v1 = v[i-1]; v2 = v[i]
        if abs(v1 + v2) < minSum:
            minSum = abs(v1 + v2)
            if v1 < v2:
                li1 = v1; li2 = v2
            else:
                li1 = v2; li2 = v1

    print(li1, end=" ")
    print(li2)

solution()