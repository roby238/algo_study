import sys
def solution():
    read = sys.stdin.readline
    s, n, k, r1, r2, c1, c2 = map(int, read().rstrip().split())
    arr = [[0 for _ in range(c2-c1 + 1)] for _ in range(r2-r1 + 1)]

    def simulate(size, y, x):
        if (size <= 1) or (r2 < y) or (c2 < x) or (y + size <= r1) or (x + size <= c1):
            return
        nextSize = size // n
        margin = (size - nextSize * k) // 2
        centersy = margin + y
        centerey = size - margin + y
        centersx = margin + x
        centerex = size - margin + x
        newy = max(r1, centersy)
        newx = max(c1, centersx)

        for i in range(newy, centerey):
            if i > r2: break
            for j in range(newx, centerex):
                if j > c2: break
                arr[i - r1][j - c1] = 1

        for i in range(y, y + size, nextSize):
            for j in range(x, x + size, nextSize):
                if centersy <= i < centerey and centersx <= j < centerex:
                    continue
                simulate(nextSize, i, j)

    simulate(pow(n,s), 0, 0)

    for i in range(r2-r1+1):
        answer = ""
        for j in range(c2-c1+1):
            answer += str(arr[i][j])
        print(answer)

solution()