from collections import deque

n = int(input())
area,height = [],[]
a_max , safe_max = 0,1
dx,dy = (-1,0,1,0) , (0,1,0,-1)

def bfs(x,y,h,visited):
  q = deque()
  visited[x][y] = True
  q.append((x,y))
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if not (0 <= nx < n and 0 <= ny < n) :
        continue
      if visited[nx][ny]:
        continue
      if area[nx][ny] > h:
        visited[nx][ny] = True
        q.append((nx,ny))
  return 1

for i in range(n):
  a = list(map(int,input().split()))
  area.append(a)
  for j in range(n):
    if area[i][j] in height: continue
    else: height.append(area[i][j])

for h in height:
  cnt = 0
  visited = [[False for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if area[i][j] > h and not visited[i][j]: cnt += bfs(i,j,h,visited)
  safe_max = max(cnt,safe_max)     
  
print(safe_max)
