import sys
from collections import deque
input = sys.stdin.readline

# 상 하 좌 우
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
 
def F_bfs(): # 불 번지기
  while Fq:
    x ,y = Fq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if not (0 <= nx < R and 0 <= ny < C) : # 미로 밖을 벗어나면 무시
        continue
      if miro[nx][ny] == '#' or Fmove[nx][ny]: # 벽이거나 이미 불이 번진 곳이면 무시
        continue
      Fmove[nx][ny] = Fmove[x][y] + 1 # 거리 1 더해주기
      Fq.append((nx,ny)) # 큐에 삽입

def J_bfs():
  while Jq:
    x,y = Jq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if not (0 <= nx < R and 0 <= ny < C) : # 미로 밖을 벗어나면 탈출한 것임으로 거리 출력
        print(Jmove[x][y])
        return
      if miro[nx][ny] == '#' or Jmove[nx][ny]: # 전진했는데 벽이거나 이미 방문한 곳이면 무시
        continue
      # 지훈이 가기 전에 불이 도달하거나 이미 불이 도달한 곳이라면 무시
      if Jmove[x][y] + 1 >= Fmove[nx][ny] and Fmove[nx][ny]:
        continue
      Jmove[nx][ny] = Jmove[x][y] +1 #거리 증가시키기
      Jq.append((nx,ny)) #다음 좌표 큐에 삽입
  print("IMPOSSIBLE") #큐에 아무 것도 없으면 불가능 출력
  return
        
        
R,C = map(int,input().split()) # 미로 크기 입력받기
      
miro = [] # 입력받을 미로 리스트 선언

Jq = deque() # 지훈 움직임
Fq = deque() # 불 움직임

Jmove = [[0]*C for _ in range(R)] # 지훈 움직임 계산할 리스트 
Fmove = [[0]*C for _ in range(R)] # 불 움직임 계산할 리스트 

for i in range(R):
  miro.append(list(input().strip())) # 미로 정보 입력받기
  for j in range(C):
    if miro[i][j] == 'J': # 초기 J 찾기
      Jq.append((i,j)) #지훈이 시작점 큐에 삽입
      Jmove[i][j] = 1 # 시작점 좌표에 1 지정 (거리 계산 위해)
    elif miro[i][j] == 'F': # 불의 시작점 찾기
      Fq.append((i,j)) # 불의 시작점 큐에 삽입
      Fmove[i][j] = 1 # 시작점 좌표에 1 지정 ( 거리 계산 위해)

F_bfs()
J_bfs()
