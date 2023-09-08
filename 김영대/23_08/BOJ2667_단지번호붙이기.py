import sys
from collections import deque
def solution():
    read = sys.stdin.readline
    dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)
    n = int(read())
    m = [read() for _ in range(n)]
    v = [[0 for _ in range(n)] for _ in range(n)]
    c = []
    q = deque()

    def bfs(y, x):
        count = 1
        q.append((y, x))
        v[y][x] = 1
        while(q):
            sy, sx = q.popleft()
            for k in range(4):
                ny, nx = sy + dy[k], sx + dx[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                if m[ny][nx] == '0' or v[ny][nx]: continue

                v[ny][nx] = 1
                count += 1
                q.append((ny, nx))
        c.append(count)

    for i in range(n):
        for j in range(n):
            if m[i][j] == '0' or v[i][j]: continue
            bfs(i, j)

    c.sort()

    print(len(c))
    for num in c:
        print(num)

solution()