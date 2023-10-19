import sys
def solutionProc():
    read = sys.stdin.readline
    n, m = map(int, read().split())
    board = [list(map(int, read().split())) for _ in range(n)]
    moveBuf = [list(map(int, read().split())) for _ in range(m)]
    dy, dx = (0, -1, -1, -1, 0, 1, 1, 1), (-1, -1, 0, 1, 1, 1, 0, -1)

    # rain process
    def rainProc(cldBuf):
        tmpBoard = [[0 for _ in range(n)] for _ in range(n)]
        cldBoard = [[False for _ in range(n)] for _ in range(n)]
        for cld in cldBuf:
            board[cld[0]][cld[1]] += 1
            cldBoard[cld[0]][cld[1]] = True
        for cld in cldBuf:
            cross = [[cld[0] - 1, cld[1] - 1], [cld[0] - 1, cld[1] + 1],
                     [cld[0] + 1, cld[1] - 1], [cld[0] + 1, cld[1] + 1]]
            crossWaterCnt = 0
            for cr in cross:
                if cr[0] < 0 or cr[0] >= n or \
                        cr[1] < 0 or cr[1] >= n: continue
                if board[cr[0]][cr[1]]: crossWaterCnt += 1
            tmpBoard[cld[0]][cld[1]] += crossWaterCnt

        for cld in cldBuf:
            board[cld[0]][cld[1]] += tmpBoard[cld[0]][cld[1]]

        newCldBuf = []
        for i in range(n):
            for j in range(n):
                if cldBoard[i][j]: continue

                if board[i][j] >= 2:
                    newCldBuf.append([i, j])
                    board[i][j] -= 2
        return newCldBuf

    # move cloud process
    def moveProc(cldBuf, moveIdx):
        d, s = moveBuf[moveIdx]
        for j in range(len(cldBuf)):
            cldBuf[j][0] = (cldBuf[j][0] + dy[d - 1] * s) % n
            cldBuf[j][1] = (cldBuf[j][1] + dx[d - 1] * s) % n

    # move cloud and rain process
    def moveAndRainProc():
        cldBuf = [[n - 2, 0], [n - 2, 1], [n - 1, 0], [n - 1, 1]]

        for i in range(m):
            # move
            moveProc(cldBuf, i)
            # rain
            cldBuf = rainProc(cldBuf)

    def cntWaterProc():
        res = 0
        for i in range(n):
            for j in range(n):
                res += board[i][j]
        return res

    moveAndRainProc()
    print(cntWaterProc())

solutionProc()









