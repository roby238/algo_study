import sys
sys.setrecursionlimit(10**6)

N , M = map(int,input().split())

cheese = [[0 for _ in range(M)] for _ in range(N)]
time = 0

dx = (-1,0,1,0)
dy = (0,1,0,-1)

def melting(x,y):
  cnt = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if cheese[nx][ny] == 2: cnt +=1
    else: continue
  return cnt

def outside(x,y,visited):
  visited[x][y] = True
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx > N-1 or ny > M-1 or cheese[nx][ny] == 1 or visited[nx][ny]:
      continue
    else:
      cheese[nx][ny] = 2
      visited[nx][ny] = 2
      outside(nx,ny,visited)

for i in range(N):
  c = list(input().split())
  for j in range(M):
    cheese[i][j] = int(c[j])
    if i == 0 or j == 0 or i == N-1 or j == M-1:
       cheese[i][j] = 2

while True:
  visited = [[False for _ in range(M)] for _ in range(N)]
  outside(0,0,visited)
      
  melt = []
  for i in range(N):
    for j in range(M):
      if cheese[i][j] == 1:
        if melting(i,j) >= 2:
          melt.append((i,j))
      else: continue
        
  if len(melt) == 0:
    print(time)
    break
  else:
    for x,y in melt:
      cheese[x][y] = 0
    time+=1
