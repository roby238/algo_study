import sys

def solutionProc():
    read = sys.stdin.readline
    n = int(read())
    values = [list(map(int, read().split())) for _ in range(n)]
    minVal = float("inf")

    for k in range(3):
        dp = [[float("inf") for _ in range(3)] for _ in range(n)]
        dp[0][k] = values[0][k]
        for i in range(0, n - 1):
            for j in range(3):
                dp[i + 1][(j + 1) % 3] = min(dp[i][j] + values[i + 1][(j + 1) % 3], dp[i + 1][(j + 1) % 3])
                dp[i + 1][(j - 1) % 3] = min(dp[i][j] + values[i + 1][(j - 1) % 3], dp[i + 1][(j - 1) % 3])
        dp[n - 1][k] = float("inf")
        minVal = min(minVal, dp[n - 1][(k + 1) % 3], dp[n - 1][(k - 1) % 3])
        #print(dp)

    print(minVal)

solutionProc()