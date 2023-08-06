import sys
from collections import deque

def solution():
    read = sys.stdin.readline
    r, c = map(int, read().split())
    ans = 0; di = (0, 0, 1, -1); dj = (1, -1, 0, 0)
    visit = [[0 for _ in range(c)] for _ in range(r)]
    trsMap = [' ' for _ in range(r)]
    for i in range(r):
        trsMap[i] = read().rstrip()

    def bfs(i, j):
        check = i * c + j + 1
        visit[i][j] = check
        nq = deque()
        nq.append([i, j])
        step = 0
        while len(nq):
            pq = nq
            nq = deque()
            flag = False
            while len(pq):
                si, sj = pq.popleft()
                for k in range(4):
                    ni = si + di[k]
                    nj = sj + dj[k]
                    if ni < 0 or r <= ni or nj < 0 or c <= nj or trsMap[ni][nj] == 'W' or visit[ni][nj] == check:
                        continue
                    visit[ni][nj] = check
                    nq.append([ni, nj])
                    flag = True
            if flag:
                step += 1
        return step

    for i in range(r):
        for j in range(c):
            if trsMap[i][j] == 'W':
                continue
            ans = max(ans, bfs(i, j))

    print(ans)

solution()