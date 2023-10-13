import sys
def solution():
    read = sys.stdin.readline
    n = int(read())
    minDiff = float("inf")
    board = [list(map(int, read().split())) for _ in range(n)]

    def divisionProc(y, x, d1, d2):
        p = [0, 0, 0, 0, 0]
        for i in range(n):
            for j in range(n):
                if i < y and j <= x + d1 and i + j < y + x:
                    p[0] += board[i][j]
                elif i <= y - d1 + d2 and x + d1 < j and (i - j < y - x - 2 * d1):
                    p[1] += board[i][j]
                elif y - d1 + d2 < i and x + d2 <= j and (y + x + 2 * d2 < i + j):
                    p[2] += board[i][j]
                elif y <= i and j < x + d2 and y - x < i - j:
                    p[3] += board[i][j]
                else:
                    p[4] += board[i][j]
        return max(p) - min(p)

    for i in range(1, n - 1):
        for j in range(n - 2):
            for d1 in range(1, i + 1):
                for d2 in range(1, n):
                    if n <= j + d1 + d2 or n <= i + d2: break
                    minDiff = min(minDiff, divisionProc(i, j, d1, d2))
    print(minDiff)
solution()