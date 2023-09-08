import sys
from collections import deque
read = sys.stdin.readline
def solution():
    w, h = map(int, read().split())
    cObj = []
    m = []
    for i in range(h):
        m.append(read())
        for j in range(w):
            if m[i][j] == 'C':
                cObj.append([i, j, 5, 0])
    v = [[[98765432 for _ in range(4)] for _ in range(w)] for _ in range(h)]
    q = deque()

    def bfs():
        dy = [1, -1, 0, 0]
        dx = [0, 0, 1, -1]
        q.append(cObj[0])
        for i in range(4):
            v[cObj[0][0]][cObj[0][1]][i] = 0
        while(q):
            [sy, sx, sd, sm] = q.popleft()
            for k in range(4):
                ny, nx = sy + dy[k], sx + dx[k]
                if ny < 0 or ny >= h or nx < 0 or nx >= w: continue
                if m[ny][nx] == '*': continue
                mirror = sm
                if sd != k: mirror += 1
                if(v[ny][nx][k] <= mirror): continue
                v[ny][nx][k] = mirror
                q.append([ny, nx, k, mirror])

    bfs()
    ans = 98765432
    for i in range(4):
        ans = min(ans, v[cObj[1][0]][cObj[1][1]][i] - 1)
    print(ans)

solution()
