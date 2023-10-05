import sys

def solution():
    read = sys.stdin.readline
    n, m, t = map(int, read().split())
    roundBd = [list(map(int, read().split())) for _ in range(n)]
    #print(roundBd)
    turnInfo = [list(map(int, read().split())) for _ in range(t)]
    #print(turnInfo)
    turnPtr = [0 for _ in range(n)]

    def turnProc(x, d, k):
        for i in range(x - 1, n, x):
            if d:
                turnPtr[i] += k
                if turnPtr[i] >= m: turnPtr[i] -= m
            else:
                turnPtr[i] -= k
                if turnPtr[i] < 0: turnPtr[i] += m

    def meanProc():
        sum, num = 0, 0
        for i in range(n):
            for j in range(m):
                if not roundBd[i][j]: continue

                sum += roundBd[i][j]
                num += 1

        if not num: return
        mean = sum / num

        for i in range(n):
            for j in range(m):
                if not roundBd[i][j]: continue

                if mean > roundBd[i][j]:
                    roundBd[i][j] += 1
                elif mean < roundBd[i][j]:
                    roundBd[i][j] -= 1

    def sameProc():
        isSame = False
        rmList = []
        for i in range(n):
            for j in range(m):
                target = roundBd[i][j]
                if not target: continue

                right, up = -1, -1
                isSameNow = False
                right = roundBd[i][(j + 1) % m]
                if target == right:
                    isSameNow = True
                    rmList.append([i, (j + 1) % m])
                if i + 1 < n:
                    if (j + turnPtr[i + 1] - turnPtr[i]) >= m \
                            or (j + turnPtr[i + 1] - turnPtr[i]) < 0:
                        up = roundBd[i + 1][(j + turnPtr[i + 1] - turnPtr[i]) % m]
                    else:
                        up = roundBd[i + 1][j + turnPtr[i + 1] - turnPtr[i]]

                    if target == up:
                        isSameNow = True
                        if (j + turnPtr[i + 1] - turnPtr[i]) >= m \
                                or (j + turnPtr[i + 1] - turnPtr[i]) < 0:
                            rmList.append([i + 1, (j + turnPtr[i + 1] - turnPtr[i]) % m])
                        else:
                            rmList.append([i + 1, j + turnPtr[i + 1] - turnPtr[i]]);

                if isSameNow:
                    rmList.append([i, j])
                    isSame = True
        if isSame:
            for rmTarget in rmList:
                roundBd[rmTarget[0]][rmTarget[1]] = 0
        else: meanProc()

        sum = 0
        for i in range(n):
            for j in range(m):
                sum += roundBd[i][j]
        return sum

    def simulation():
        sum = 0
        for i in range(t):
            turnProc(turnInfo[i][0], turnInfo[i][1], turnInfo[i][2])
            sum = sameProc()
        return sum

    print(simulation())

solution()