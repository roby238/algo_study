import sys
globalPaperCnt = float("inf")
def solution():
    read = sys.stdin.readline
    board = [list(map(int, read().split())) for _ in range(10)]
    papers = [0, 0, 0, 0, 0, 0]
    #print(board)
    def isPossibleToAttach(y, x, s):
        for i in range(s):
            for j in range(s):
                if not board[y + i][x + j]: return False
        return True

    def attachOrDetachPaper(y, x, s, b):
        for i in range(s):
            for j in range(s):
                board[y+i][x + j] = b

    def dfsProc(y, x, currPaperCnt):
        global globalPaperCnt
        while not board[y][x]:
            x += 1
            if x >= 10:
                y += 1
                if y >= 10:
                    globalPaperCnt = min(globalPaperCnt, currPaperCnt)
                    return
                x = 0

        if globalPaperCnt <= currPaperCnt: return

        for s in range(1, 6):
            if x + s > 10 or y + s > 10 or papers[s] == 5: continue

            if isPossibleToAttach(y, x, s):
                attachOrDetachPaper(y, x, s, 0)
                papers[s] += 1
                dfsProc(y, s, currPaperCnt + 1)
                attachOrDetachPaper(y, x, s, 1)
                papers[s] -= 1

    dfsProc(0, 0, 0)
    global globalPaperCnt
    if globalPaperCnt == float("inf"): globalPaperCnt = -1
    print(globalPaperCnt)

solution()