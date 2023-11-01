import sys
def solutionProc():
    read = sys.stdin.readline
    r, c, t = map(int, read().split())
    global room
    room = [list(map(int, read().split())) for _ in range(r)]
    dy, dx = (0, -1, 0, 1), (1, 0, -1, 0)

    def diffuseProc():
        global room
        newRoom = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if room[i][j] > 0:
                    dirCnt = 0
                    for k in range(4):
                        if i + dy[k] < 0 or j + dx[k] < 0 or i + dy[k] >= r or j + dx[k] >= c\
                                                                    or room[i + dy[k]][j + dx[k]] == -1: continue
                        dirCnt += 1
                        newRoom[i + dy[k]][j + dx[k]] += room[i][j] // 5
                    newRoom[i][j] += room[i][j] - (room[i][j] // 5) * dirCnt
                elif room[i][j] == -1:
                    newRoom[i][j] = -1
        room = newRoom

    def cycleProc(i, j, clockwise):
        newRoom = [[0 for _ in range(c)] for _ in range(r)]
        si, sj, d = i, j, 0
        while 1:
            if j + dx[d] >= c or j + dx[d] < 0 or i + dy[d] < 0 or i + dy[d] >= r:
                if not clockwise: d = (d + 1) % 4
                else: d = (d - 1) % 4

            if room[i + dy[d]][j + dx[d]] == -1: break
            newRoom[i + dy[d]][j + dx[d]] = room[i][j]
            i += dy[d]
            j += dx[d]

        i, j = si, sj
        d = 0
        while 1:
            if j + dx[d] >= c or j + dx[d] < 0 or i + dy[d] < 0 or i + dy[d] >= r:
                if clockwise: d = (d - 1) % 4
                else: d = (d + 1) % 4

            if room[i][j] == -1: break
            room[i][j] = newRoom[i][j]
            i += dy[d]
            j += dx[d]

    def cleanProc():
        airIdx = 0
        for i in range(r):
            if room[i][0] == -1:
                airIdx = i
                break

        cycleProc(airIdx, 1, 0)
        cycleProc(airIdx + 1, 1, 1)

    def repeatPerSecondProc():
        for _ in range(t):
            diffuseProc()
            cleanProc()
        ans = 0
        for i in range(r):
            for j in range(c):
                ans += room[i][j]
        print(ans + 2)

    repeatPerSecondProc()

solutionProc()