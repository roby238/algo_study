from collections import deque

dx = (-1,0,1,0)
dy = (0,1,0,-1)

def bfs(x,y):
  q = deque()
  q.append((x,y))
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if not (0 <= nx < n and 0 <= ny < n):
        continue
      if visited[nx][ny] > visited[x][y] + p[nx][ny]:
        visited[nx][ny] = visited[x][y] + p[nx][ny]
        q.append((nx,ny))

cnt = 1
while True:
  n = int(input())
  if n == 0: break
  p = []
  visited = [[int(1e9)]* n for _ in range(n)]
  for _ in range(n):
    p.append(list(map(int,input().split())))
  visited[0][0] = p[0][0]
  bfs(0,0)
  print(f'Problem {cnt}: {visited[n - 1][n - 1]}')
  cnt+=1
