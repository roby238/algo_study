import sys
def solution():
    read = sys.stdin.readline
    n, d, k, c = map(int, read().split())
    sushi = [int(read()) for _ in range(n)]
    sushiCnt = [0 for _ in range(d + 1)]
    maxCnt = 0
    for i in range(n):
        for j in range(1, d + 1): sushiCnt[j] = 0
        sushiCnt[c] = 1
        cnt, flag = k + 1, False
        for j in range(i, i + k):
            if j >= n:
                if sushiCnt[sushi[j - n]]:
                    cnt -= 1
            else:
                if sushiCnt[sushi[j]]:
                    cnt -= 1

            if cnt <= maxCnt:
                flag = True
                break

            if j >= n: sushiCnt[sushi[j - n]] += 1
            else: sushiCnt[sushi[j]] += 1
        if flag: continue
        maxCnt = max(maxCnt, cnt)
    print(maxCnt)

solution()