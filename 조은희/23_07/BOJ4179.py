import sys
from collections import deque
input = sys.stdin.readline

def escape_map():
    # 불 이동
    while fire:
        x, y = fire.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C:
                if not fire_visit[nx][ny] and map[nx][ny] != '#': # 불이 퍼지지 않았고 벽이 아닐 경우
                    fire_visit[nx][ny] = fire_visit[x][y] + 1
                    fire.append((nx, ny))

    # 지훈 이동
    while jihun:
        x, y = jihun.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C:
                if not jihun_visit[nx][ny] and map[nx][ny] != '#': # 방문하지 않았고 벽이 아닐 경우
                    if not fire_visit[nx][ny] or fire_visit[nx][ny] > jihun_visit[x][y] + 1:
                        jihun_visit[nx][ny] = jihun_visit[x][y] + 1
                        jihun.append((nx, ny))
            else: # 탈출한 경우
                print(jihun_visit[x][y] + 1)
                return 

    # 탈출하지 못 한 경우
    print("IMPOSSIBLE")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 입력 받기
R, C = map(int, input().split())
map = [list(input().strip()) for _ in range(R)]
fire, jihun = deque(), deque()
fire_visit, jihun_visit = [[-1] * C for _ in range(R)], [[-1] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if map[i][j] == 'F':
            fire.append((i, j))
            fire_visit[i][j] = 0
        elif map[i][j] == 'J':
            jihun.append((i, j))
            jihun_visit[i][j] = 0

# 2. 미로 탈출 시작
escape_map()
