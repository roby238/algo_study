from collections import deque

n = int(input())
area = [[0 for _ in range(n)] for _ in range(n)]
a_max , safe_max = 0,0
dx,dy = (-1,0,1,0) , (0,1,0,-1)

def bfs(x,y):
  q = deque()
  visited[x][y] = True
  q.append((x,y))
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if area[nx][ny] > am and not visited[nx][ny]:
          visited[nx][ny] = True
          q.append((nx,ny))
  return 1

for i in range(n):
  a = list(map(int,input().split()))
  for j in range(n):
    area[i][j] = int(a[j])
    a_max  = max(area[i][j],a_max)

for am in range(1,a_max+1):
  cnt = 0
  visited = [[False for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if area[i][j] > am and not visited[i][j]:
        cnt += bfs(i,j)

  if not cnt: cnt = 1
  safe_max = max(cnt,safe_max)
        
print(safe_max)
