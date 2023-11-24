from collections import deque
from itertools import combinations

dx = (0,1,0,-1)
dy = (1,0,-1,0)

N,M = map(int,input().split())

p = [list(map(int,input().split())) for _ in range(N)]

wall = []
virus_sub = []

for x in range(N) :
    for y in range(N) :
        if p[x][y] == 1 :
            wall.append((x,y))
        elif p[x][y] == 2 :
            virus_sub.append((x,y))
            p[x][y] = 0

result = 10e9
for virus in combinations(virus_sub,M) :
    visited = [[0]*N for _ in range(N)]
    v = deque(virus[:])
    for x,y in virus :
        p[x][y] = 2 
        visited[x][y] = 1
    cnt = M+len(wall)
    while v :
        x,y = v.popleft()
        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and p[nx][ny] == 0 :
                visited[nx][ny] = visited[x][y] + 1 
                v.append((nx,ny))
                cnt += 1 
            if N**2 - cnt == 0:
                tmp = 0
                for i in range(N) :
                    tmp = max(max(visited[i]),tmp)
                if tmp<result :
                    result = tmp 
                break 
    for x,y in virus :
        p[x][y] = 0

if result>=10e9 :
    print(-1)
else :
    print(result-1)
