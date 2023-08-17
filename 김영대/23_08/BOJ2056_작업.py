import sys
def solution():
    read = sys.stdin.readline
    N = int(read())
    task = [[] for _ in range(N + 1)]
    dp = [0 for _ in range(N + 1)]
    maxTime = 0

    for i in range(1, N + 1):
        line = list(map(int, read().split()))
        dp[i] = line[0]
        if line[1] > 0:
            task[i] = line[2:]

    for i in range(1, N + 1):
        if task[i]:
            tmp = 0
            for t in task[i]:
                tmp = max(tmp, dp[t])
            dp[i] += tmp
        maxTime = max(maxTime, dp[i])

    print(maxTime)

solution()