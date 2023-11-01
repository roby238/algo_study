import sys
from collections import deque
def solutionProc():
    read = sys.stdin.readline
    n = int(read())
    dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)
    def isValid(y, x):
        if y >= h or y < 0 or x >= w or x < 0: return False
        return True
    def bfs(fnq, hnq):
        step = 0
        while hnq:
            fpq = fnq.copy()
            fnq = deque()
            while fpq:
                sy, sx = fpq.popleft()
                for k in range(4):
                    ny, nx = sy + dy[k], sx + dx[k]
                    if not isValid(ny, nx) or visit[ny][nx]: continue
                    visit[ny][nx] = 1
                    fnq.append((ny, nx))

            hpq = hnq.copy()
            hnq = deque()
            while hpq:
                sy, sx = hpq.popleft()
                for k in range(4):
                    ny, nx = sy + dy[k], sx + dx[k]
                    if not isValid(ny, nx): return step + 1
                    if visit[ny][nx]: continue
                    visit[ny][nx] = 1
                    hnq.append((ny, nx))
            step += 1

        return -1

    for _ in range(n):
        w, h = map(int, read().split())
        building = []
        fnq = deque()
        hnq = deque()
        visit = [[0 for _ in range(w)] for _ in range(h)]

        for i in range(h):
            building.append(list(read().rstrip()))
            for j in range(w):
                if building[i][j] == '@':
                    hnq.append((i, j))
                    visit[i][j] = 1
                elif building[i][j] == '*':
                    fnq.append((i, j))
                    visit[i][j] = 1
                elif building[i][j] == '#':
                    visit[i][j] = 1

        res = bfs(fnq, hnq)
        if res == -1: print("IMPOSSIBLE")
        else: print(res)

solutionProc()