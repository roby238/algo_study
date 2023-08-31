import sys
from collections import deque
def solution():
    read = sys.stdin.readline
    n, k = map(int, read().split())
    dp = [float("inf") for _ in range(100001)]
    q = deque()

    def bfs():
        dp[n] = 0
        q.append(n)
        while q:
            start = q.popleft()
            if start == k: return

            if start < 100000 and dp[start] + 1 < dp[start + 1]:
                dp[start + 1] = dp[start] + 1
                q.append(start + 1)
            if start > 0 and dp[start] + 1 < dp[start - 1]:
                dp[start - 1] = dp[start] + 1
                q.append(start - 1)
            if start <= 50000 and dp[start] < dp[2 * start]:
                dp[2 * start] = dp[start]
                q.append(2 * start)

    bfs()

    print(dp[k])

solution()