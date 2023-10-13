import sys
globalSand = 0
def solution():
    read = sys.stdin.readline
    n = int(read())
    sand = [[0 for _ in range(n + 1)]] + [[0] + list(map(int, read().split())) for _ in range(n)]
    dy, dx = (0, 1, 0, -1), (-1, 0, 1, 0)
    pos = [[0, 0] for _ in range(10)]

    def isValid(y, x):
        if y < 1 or y > n or x < 1 or x > n: return False
        return True

    def windProc(y, x, d):
        global globalSand
        originSand = sand[y][x]
        sandK = (originSand // 20, originSand // 10, (originSand * 7) // 100, originSand // 50, originSand // 100)
        sandR = sand[y][x]
        for i in range(len(sandK)):
            if not i: sandR -= sandK[i]
            else: sandR -= 2 * sandK[i]

        leftY, leftX, downY, downX, rightY, rightX, upY, upX = \
            dy[d], dx[d], dy[(d + 1) % 4], dx[(d + 1) % 4], \
            dy[(d + 2) % 4], dx[(d + 2) % 4], dy[(d + 3) % 4], dx[(d + 3) % 4]

        pos[0] = [y + 2 * leftY, x + 2 * leftX]
        pos[1] = [y + leftY + upY, x + leftX + upX]
        pos[2] = [y + leftY + downY, x + leftX + downX]
        pos[3] = [y + upY, x + upX]
        pos[4] = [y + downY, x + downX]
        pos[5] = [y + 2 * upY, x + 2 * upX]
        pos[6] = [y + 2 * downY, x + 2 * downX]
        pos[7] = [y + rightY + upY, x + rightX + upX]
        pos[8] = [y + rightY + downY, x + rightX + downX]
        pos[9] = [y + leftY, x + leftX]

        for i in range(10):
            if isValid(pos[i][0], pos[i][1]):
                if i == 9: sand[pos[i][0]][pos[i][1]] += sandR
                else: sand[pos[i][0]][pos[i][1]] += sandK[(i + 1) // 2]
            else:
                if i == 9: globalSand += sandR
                else: globalSand += sandK[(i + 1) // 2]

    def moveProc():
        global globalSand
        y, x = n // 2 + 1, n // 2 + 1
        dir, dist = 0, 1
        while 1:
            for _ in range(2):
                for _ in range(dist):
                    y += dy[dir]
                    x += dx[dir]
                    windProc(y, x, dir)
                    if y == 1 and x == 1: return
                dir = (dir + 1) % 4
            dist += 1

    moveProc()
    print(globalSand)

solution()