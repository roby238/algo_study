import sys
def solution():
    read = sys.stdin.readline
    n, m, k = map(int, read().split())
    #r, c, m, s, d = [], [], [], [], []
    fire = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
    dy = (-1, -1, 0, 1, 1, 1, 0, -1)
    dx = (0, 1, 1, 1, 0, -1, -1, -1)
    for _ in range(m):
        r, c, m, s, d = map(int, read().split())
        fire[r][c].append([m, s, d])

    def moveProc():
        tmpFire = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
        for row in range(1, n + 1):
            for col in range(1, n + 1):
                for k in range(len(fire[row][col])):
                    spd = fire[row][col][k][1]
                    dir = fire[row][col][k][2]

                    newRow = row + spd * dy[dir]
                    newCol = col + spd * dx[dir]
                    if n < newRow: newRow %= n
                    if newRow < 1: newRow %= n
                    if not newRow: newRow = n
                    if n < newCol: newCol %= n
                    if newCol < 1: newCol %= n
                    if not newCol: newCol = n
                    tmpFire[newRow][newCol].append(fire[row][col][k])


        for row in range(1, n + 1):
            for col in range(1, n + 1):
                fire[row][col] = tmpFire[row][col]

    def splitProc():
        for row in range(1, n + 1):
            for col in range(1, n + 1):
                if len(fire[row][col]) >= 2:
                    msv, spd, dir = 0, 0, 0
                    for k in range(len(fire[row][col])):
                        msv += fire[row][col][k][0]
                        spd += fire[row][col][k][1]
                        dir += fire[row][col][k][2] % 2
                    newMsv = msv // 5
                    newSpd = spd // len(fire[row][col])
                    #newDir = []
                    if dir == 0 or dir == len(fire[row][col]):
                        newDir = [0, 2, 4, 6]
                    else:
                        newDir = [1, 3, 5, 7]
                    fire[row][col] = []
                    if not newMsv: continue
                    for k in range(4):
                        fire[row][col].append([newMsv, newSpd, newDir[k]])

    def sumProc():
        res = 0
        for row in range(1, n + 1):
            for col in range(1, n + 1):
                for k in range(len(fire[row][col])):
                    res += fire[row][col][k][0]
        return res

    def printProc():
        for row in range(1, n + 1):
            for col in range(1, n + 1):
                for k in range(len(fire[row][col])):
                    print(fire[row][col][k], end = " ")
                print("/", end = "")
            print(" ")

    for _ in range(k):
        moveProc()
        #printProc()
        #print(fire)
        splitProc()



    print(sumProc())

solution()