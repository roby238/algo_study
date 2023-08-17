import sys
def solution():
    read = sys.stdin.readline
    N, D = map(int, read().split())
    dp = [i for i in range(10001)]
    sc = [[] for _ in range(10001)]
    for _ in range(N):
        s, e, d = map(int, read().split())
        if e - s <= d or e > D: continue
        sc[s].append([e, d])

    tmp = -1
    for s in range(D + 1):
        if(s): tmp = dp[s - 1]
        dp[s] = min(dp[s], tmp + 1)

        if(len(sc[s]) == 0): continue

        for target in sc[s]:
            [e, d] = target
            dp[e] = min(dp[e], dp[s] + d)

    print(dp[D])

solution()