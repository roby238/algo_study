import sys
def solution():
    read = sys.stdin.readline
    n, m = map(int, read().split())
    list = [int(read()) for _ in range(n)]
    list.sort()
    s, e = 0, 1
    minDiff = float("inf")
    while s < n:
        if e < n:
            diff = list[e] - list[s]
        else:
            diff = list[n - 1] - list[s]

        if diff < m:
            if e < n - 1:
                e += 1
            else:
                s += 1
            continue
        elif diff == m:
            minDiff = diff
            break
        minDiff = min(minDiff, diff)
        s += 1
    print(minDiff)

solution()