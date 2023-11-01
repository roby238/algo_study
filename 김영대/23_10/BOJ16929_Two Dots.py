import sys
def solutionProc():
    read = sys.stdin.readline
    n, m = map(int, read().split())
    board = [read().rstrip() for _ in range(n)]
    visit = [[False for _ in range(m)] for _ in range(n)]
    dy, dx = (1, 0, -1, 0), (0, 1, 0, -1)

    def dfsProc(sy, sx, y, x, d, cnt):
        if sy == y and sx == x and cnt >= 4:
            print("Yes")
            exit()

        sameCnt = 0
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if ny < 0 or ny >= n or nx < 0 or nx >= m: continue
            if board[y][x] == board[ny][nx]: sameCnt += 1
        if sameCnt < 2: return 2

        for k in range(d, d + 4):
            nk = k % 4
            ny, nx = y + dy[nk], x + dx[nk]
            if ny < 0 or ny >= n or nx < 0 or nx >= m \
                    or visit[ny][nx] or board[y][x] != board[ny][nx]: continue

            visit[ny][nx] = True
            dfsProc(sy, sx, ny, nx, (d + 1) % 4, cnt + 1)
            visit[ny][nx] = False

    for i in range(n):
        for j in range(m):
            dfsProc(i, j, i, j, 0, 0)
            visit[i][j] = True

    print("No")

solutionProc()