import sys
def solution():
    read = sys.stdin.readline
    n, m = map(int, read().split())
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    friends = [0 for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, read().split())
        if a < b:
            dp[a][b] = 1
        else:
            dp[b][a] = 1
        friends[a] += 1
        friends[b] += 1
    friendsSum = float("inf")

    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if not dp[i][j]: continue
            for k in range(j + 1, n + 1):
                if not dp[j][k] or not dp[i][k]: continue
                friendsSum = min(friendsSum, friends[i] + friends[j] + friends[k] - 6)

    if friendsSum == float("inf"):
        print(-1)
    else:
        print(friendsSum)
solution()