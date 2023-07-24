from collections import deque

def bfs(h):
  num = 0
  q = deque()
  q.append(h)
  visited[h] = True

  while q:
    for i in q:
      if num: white.append(i)
      else: blue.append(i)
    for _ in range(len(q)):
      h = q.popleft()
      for j in hate[h]:
        if not visited[j]:
          visited[j] = True
          q.append(j)
    num^=1
    
n = int(input())
hate,blue,white = [],[],[]
hate.append([])
for i in range(n):
  info = list(map(int,input().split()))
  hate.append(info[1:])

visited = [False]*(n+1)

for i in range(1,n+1):
  if not visited[i]:
    bfs(i)

print(len(blue))
print(*sorted(blue))
print(len(white))
print(*sorted(white))
