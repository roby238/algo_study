# 두 동전

import sys

from collections import deque

def Solution():
    def move(d, coin):
        ty, tx = coin[0] + dt[d][0], coin[1] + dt[d][1]
        if n > ty >= 0 and m > tx >= 0:
            if grid[ty][tx] != "#":
                return ((0, ty, tx))
            else:
                return ((0, coin[0], coin[1]))
        else:
            return ((1, ty, tx))

    inp = sys.stdin.readline

    n, m = map(int, inp().split())
    grid = []
    coins = [0]
    visit = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]


    dt = ((-1, 0), (0, 1), (1, 0), (0, -1))

    for y in range(n):
        grid.append(inp().strip())
        for x in range(m):
            if grid[-1][x] == "o":
                coins.append(y)
                coins.append(x)
    visit[coins[1]][coins[2]][coins[3]][coins[4]] = True
    dq = deque()
    dq.append(coins)

    for _ in range(10):
        tmp = deque()
        while dq:
            round, y1, x1, y2, x2 = dq.popleft()
        
            for d in range(4):
                fall1, ty1, tx1 = move(d, (y1, x1))
                fall2, ty2, tx2 = move(d, (y2, x2))

                if ty1 == ty2 and tx1 == tx2:
                    continue
                if (s:=fall1 + fall2) == 1:
                    print(round + 1)
                    exit(0)
                if s == 0 and not visit[ty1][tx1][ty2][tx2]:
                    visit[ty1][tx1][ty2][tx2] = True
                    tmp.append((round + 1, ty1, tx1, ty2, tx2))
        dq = tmp
    print(-1)

if __name__ == "__main__":
    Solution()

# https://www.acmicpc.net/problem/16197