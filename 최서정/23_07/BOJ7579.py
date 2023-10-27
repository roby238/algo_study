N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
 
max_cost = (sum(cost)+1)
dp = [[0]*max_cost for _ in range(N+1)]
_min = max_cost
for i in range(1, N+1):
    for j in range(len(dp[0])):
        if j < cost[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i-1]] + memory[i-1])
        if dp[i][j] >= M and _min > j:
            _min = j
 
print(_min)
