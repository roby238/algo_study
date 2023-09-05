import sys
from collections import deque
def solution():
    read = sys.stdin.readline
    row, col = map(int, read().split())
    m = [[1 for _ in range(col + 2)] for _ in range(row + 2)]
    v = [[0 for _ in range(col + 2)] for _ in range(row + 2)]
    for i in range(1, row + 1):
        m[i][1:col + 1] = list(map(int, read().split()))
    dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)
    space = []

    def bfs1(y, x): # 너비우선탐색: 2개 이하의 열린 공간 좌표 찾기
        q = deque()
        q.append((y, x))
        v[y][x] = 1
        tmp = []
        while q:
            sy, sx = q.popleft()
            for k in range(4):
                ny, nx = sy + dy[k], sx + dx[k]
                if v[ny][nx]: continue

                if not m[ny][nx]:
                    if not [ny, nx] in tmp:
                        tmp.append([ny, nx])
                elif m[ny][nx] == 2:
                    q.append((ny, nx))
                    v[ny][nx] = 1
        if len(tmp) > 2: return # 열린 공간이 2개보다 많을 때
        for pos in tmp:
            if not pos in space:
                space.append(pos)

    for i in range(1, row + 1): # loop에서 BFS
        for j in range(1, col + 1):
            if m[i][j] == 2 and not v[i][j]:
                bfs1(i, j)

    def bfs2(y, x, n): # #너비우선탐색: 닫힌 공간에서 적 돌의 개수 찾기
        q = deque()
        q.append((y, x))
        v[y][x] = n
        target = 1
        flag = False
        while q:
            sy, sx = q.popleft()
            for k in range(4):
                ny, nx = sy + dy[k], sx + dx[k]
                if v[ny][nx] == n:
                    continue
                if m[ny][nx] == 0: flag = True # 닫힌 공간이 아닐 때
                elif m[ny][nx] == 2:
                    q.append((ny, nx))
                    v[ny][nx] = n
                    target += 1
        if flag: return 0 # 닫힌 공간이 아닐 때 개수 0 return
        return target

    ans = 0
    cnt = 2
    if len(space) > 1: # 2개 이상의 좌표군에 대해
        for i in range(len(space)):
            m[space[i][0]][space[i][1]] = 1 # 벽 세우기
            for j in range(i + 1, len(space)):
                m[space[j][0]][space[j][1]] = 1 # 벽 세우기
                targetMax = 0
                for y in range(1, row + 1):
                    for x in range(1, col + 1):
                        if m[y][x] == 2 and v[y][x] != cnt:
                            targetMax += bfs2(y, x, cnt) # 좌표 2개를 선정해 벽을 세웠을 때 가둬지는 적 돌의 합
                ans = max(ans, targetMax) # 최대값 구하기
                cnt += 1 # v에 저장될 num 증가

                m[space[j][0]][space[j][1]] = 0 # 벽 제거
            m[space[i][0]][space[i][1]] = 0 # 벽 제거

    elif len(space) == 1: # 1개의 좌표에 대해
        m[space[0][0]][space[0][1]] = 1
        targetMax = 0
        for y in range(1, row + 1):
            for x in range(1, col + 1):
                if m[y][x] == 2 and v[y][x] != 2:
                    targetMax += bfs2(y, x, 2)
        ans = max(ans, targetMax)

    print(ans)

solution()