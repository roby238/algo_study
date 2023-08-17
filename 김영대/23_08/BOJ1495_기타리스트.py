import sys
def solution():
    read = sys.stdin.readline
    N, S, M = map(int, read().split())
    volumes = list(map(int, read().split()))
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    def dfs(d, v):
        dp[d][v] = 1
        if d == N: return

        if v + volumes[d] <= M and not dp[d + 1][v + volumes[d]]:
            dfs(d + 1, v + volumes[d])
        if 0 <= v - volumes[d] and not dp[d + 1][v - volumes[d]]:
            dfs(d + 1, v - volumes[d])

    dfs(0, S)

    for idx in range(M, -1, -1):
        if dp[N][idx]:
            print(idx)
            return

    print(-1)

solution()