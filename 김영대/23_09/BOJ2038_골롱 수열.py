def solution():
    n = int(input())
    dp = [0 for _ in range(777777)]
    golomb = [0, 1]
    dp[0], dp[1], dp[2] = 1, 1, 2
    idx, cnt = 2, 2
    while idx < 699999:
        for i in range(dp[cnt]):
            dp[idx] = cnt
            idx += 1
        cnt += 1
    idx = 1
    while golomb[idx] <= n:
        golomb.append(golomb[idx] + dp[idx])
        idx += 1
    print(idx - 1)

solution()