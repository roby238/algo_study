import sys
def solution():
    read = sys.stdin.readline
    n, m = map(int, read().split())
    dp = [[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, read().split())
        for i in range(1, n + 1):
            if i == a or i == b: continue
            if i < a < b:
                dp[i][a][b] = 1
            elif a < i < b:
                dp[a][i][b] = 1
            elif a < b < i:
                dp[a][b][i] = 1
            elif i < b < a:
                dp[i][b][a] = 1
            elif b < i < a:
                dp[b][i][a] = 1
            elif b < a < i:
                dp[b][a][i] = 1

    icecreamCount = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if not dp[i][j][k]:
                    icecreamCount += 1

    print(icecreamCount)

solution()