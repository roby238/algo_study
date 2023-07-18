A, B = map(int,input().split())
N, M = map(int,input().split())

robot,com = [], []

dx = (0,1,0,-1) 
dy = (1,0,-1,0)
dir = ('N','E','S','W')

done = True

for i in range(N):
  x,y,d = input().split()
  robot.append([int(x),int(y),d])

for _ in range(M):
  R , K , loop = input().split()
  com.append((int(R),K,int(loop)))

for R,K,loop in com:
  if not done: break
  for _ in range(loop):
    if K == 'F':
      robot[R-1][0] += dx[dir.index(robot[R-1][2])]
      robot[R-1][1] += dy[dir.index(robot[R-1][2])]
      for i in range(N):
        if i != R-1 and robot[R-1][0] == robot[i][0] and robot[R-1][1] == robot[i][1]:
            print('Robot',R,'crashes into robot',i+1)
            done = False
            break
      if not done: break       
      if 1 > robot[R-1][0] or robot[R-1][0] > A or 1 > robot[R-1][1] or robot[R-1][1] > B:
        print('Robot',R,'crashes into the wall')
        done = False
        break
    else:
      if K == 'L':
        robot[R-1][2] = dir[(dir.index(robot[R-1][2])-1)%4]
      else:
        robot[R-1][2] = dir[(dir.index(robot[R-1][2])+1)%4]              
if done: print('OK')
