import sys
from collections import deque
def solution():
    #---------------------------------------------------#
    read = sys.stdin.readline
    n, m, p = map(int, read().split()) # input : rows, cols, players
    s = list(map(int, read().split())) # input : s[i] -> steps once turn
    castle = [0 for _ in range(p)] # number of player's castles
    pos = [deque() for _ in range(p)] # positions of player castles
    dy, dx = (1, 0, -1, 0), (0, 1, 0, -1) # direction vector : read only attributes
    # board input & settings
    board = [['#' for _ in range(m + 2)]] # board for game
    for r in range(1, n + 1):
        board.append(['#'] + list(read().rstrip()) + ['#'])
        for c in range(1, m + 1):
            if board[r][c] != '.' and board[r][c] != '#':
                castle[int(board[r][c]) - 1] += 1
                pos[int(board[r][c]) - 1].append((r, c))
    board.append(['#' for _ in range(m + 2)])
    #--------------------------------------------------#
    def isValid(y, x): # is valid position to conquer
        if board[y][x] != '.': return False
        return True

    def bfsProc(player): # bfs : step
        cnt = 0
        for _ in range(s[player]):
            if not len(pos[player]): break
            q = pos[player].copy()
            pos[player].clear()
            cnt = 0
            while q:
                sy, sx = q.popleft()
                for k in range(4):
                    ny, nx = sy + dy[k], sx + dx[k]
                    if not isValid(ny, nx): continue
                    board[ny][nx] = str(player + 1)
                    pos[player].append((ny, nx))
                    cnt += 1
                    castle[player] += 1
        return cnt

    def gameProc(): # start : game for each player until end phase(no more possible node)
        cnt = 1
        while cnt:
            cnt = 0
            for i in range(p):
                cnt += bfsProc(i)
        for i in range(p):
            print(f"{castle[i]}", end = " ")
    #----------------------------------------------#
    gameProc()

solution()