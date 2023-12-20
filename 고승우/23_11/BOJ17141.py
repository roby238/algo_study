# 연구소 2

import sys
from collections import deque

def Solution():
    inp = sys.stdin.readline

    def DFS(idx, cnt):
        if cnt == m:
            set_up()
            execute()
            return
        elif idx == len(start_point):
            return
        candidates.append(start_point[idx])

        DFS(idx + 1, cnt + 1)
        candidates.pop()

        DFS(idx + 1, cnt)


    def set_up():
        for y in range(n):
            for x in range(n):
                virus[y][x] = False

    def execute():
        nonlocal minV
        q = deque(candidates)

        s = m
        time = -1
        for y, x in q:
            virus[y][x] = True
        update = True
        while update and minV > time:
            update = False
            tmp = deque()
            while q:
                y, x = q.popleft()
                for dy, dx in dt:
                    ty, tx = y + dy, x + dx
                    if n > ty >= 0 and n > tx >= 0 and not virus[ty][tx] and grid[ty][tx] != 1:
                        s += 1
                        update = True
                        virus[ty][tx] = True
                        tmp.append((ty, tx))

            q = tmp
            time += 1
        if s == target:
            minV = min(minV, time)

    dt = ((-1, 0), (0, 1), (1, 0), (0, -1))
    n, m = map(int, inp().split())

# 0: 빈칸, 1: 벽, 2: 바이러스
    grid = []
    virus = [[False] * n for _ in range(n)]

    start_point = []
    candidates = []
    target = 0
    minV = 1e9

    for y in range(n):
        grid.append(tuple(map(int, inp().split())))
        for x in range(n):
            if grid[y][x] == 2:
                start_point.append((y, x))
                target += 1
            elif grid[y][x] == 0:
                target += 1

    DFS(0, 0)
    print(minV if minV != 1e9 else -1)

if __name__ == "__main__":
    Solution()

# https://www.acmicpc.net/problem/17141