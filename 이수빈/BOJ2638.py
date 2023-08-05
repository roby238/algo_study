N, M = map(int, input().split())
out_list = [[0 for _ in range(M)] for _ in range(N)]
cheeze = []
mp = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def ckeck_out():
    global out_list
    out_list = [[0 for _ in range(M)] for _ in range(N)]
    out_list[0][0] = 1
    check = [(0, 0)]
    
    for x, y in check:
      for i in range(4):
          nx, ny = x + dx[i], y + dy[i]    
          if 0 <= nx < N and 0 <= ny < M and mp[nx][ny] == 0 and not out_list[nx][ny]:
              out_list[nx][ny] = 1
              check.append((nx, ny))

def melting():
    global cheeze
    cheezeList = cheeze
    cheeze = []

    for x, y in cheezeList:
        out_count = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if out_list[nx][ny]:
                out_count += 1

        if out_count < 2:
            cheeze.append((x, y))
        else:
            mp[x][y] = 0

mp = [list(map(int, input().split())) for _ in range(N)]
cheeze = [(i, j) for i in range(N) for j in range(M) if mp[i][j] == 1]
hour = 0

while len(cheeze) > 0:
    hour += 1
    ckeck_out()
    melting()

print(hour)