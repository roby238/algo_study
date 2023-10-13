import sys
def solution():
    read = sys.stdin.readline
    n, m = map(int, read().split())
    mem = [0] + list(map(int, read().split()))
    cost = [0] + list(map(int, read().split()))
    dp = [[0 for _ in range(10001)] for _ in range(101)]
    ans = float("inf")
    for i in range(1, n + 1):
        for j in range(10001):
            if cost[i] > j: dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - cost[i]] + mem[i], dp[i - 1][j])
                if dp[i][j] >= m:
                    ans = min(ans, j)
                    break
    print(ans)

solution()