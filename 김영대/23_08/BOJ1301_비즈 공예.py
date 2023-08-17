import sys
def solution():
    read = sys.stdin.readline
    N = int(read())
    b = [0 for _ in range(5)]
    for i in range(N): b[i] = int(read())
    dp = [[[[[[[-1 for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(6)] for _ in range(6)]

    def dfs(prev, curr, b, dp):
        if not(b[0] or b[1] or b[2] or b[3] or b[4]): return 1

        res = dp[prev][curr][b[0]][b[1]][b[2]][b[3]][b[4]]
        if res != -1: return res

        res = 0
        for k in range(N):
            if b[k] and not (prev == k or curr == k):
                b[k] -= 1
                res += dfs(curr, k, b, dp)
                b[k] += 1
        dp[prev][curr][b[0]][b[1]][b[2]][b[3]][b[4]] = res
        return res

    print(dfs(5, 5, b, dp))

solution()