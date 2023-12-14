import sys
from collections import deque

largest_block_group_info = (0, 0, (-1, -1))
visit_info = None
board_info = None
point = 0


def solution_proc():
    read = sys.stdin.readline
    n, m = map(int, read().split())
    global board_info
    board_info = [list(map(int, read().split())) for _ in range(n)]
    dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)

    def is_valid(y, x):
        if y >= n or y < 0 or x >= n or x < 0: return False
        return True

    def bfs_proc(n_block, y, x, flag):
        global visit_info
        visit_info = [[0 for _ in range(n)] for _ in range(n)]
        queue = deque()
        queue.append((y, x))
        visit_info[y][x] = 1
        rainbow_block_cnt = 0
        if not flag:
            block_cnt = 1
            base_block = (y, x)
        else:
            board_info[y][x] = -2
        while queue:
            sy, sx = queue.popleft()
            for k in range(4):
                ny, nx = sy + dy[k], sx + dx[k]
                if not is_valid(ny, nx): continue
                if visit_info[ny][nx]: continue
                if board_info[ny][nx] <= -1: continue
                if board_info[ny][nx] != n_block and board_info[ny][nx] != 0: continue
                visit_info[ny][nx] = 1
                queue.append((ny, nx))
                if not flag:
                    block_cnt += 1
                    if board_info[ny][nx] == n_block:
                        if base_block[0] > ny:
                            base_block = (ny, nx)
                        elif base_block[0] == ny and base_block[1] > nx:
                            base_block = (ny, nx)
                    elif not board_info[ny][nx]:
                        rainbow_block_cnt += 1
                else:
                    board_info[ny][nx] = -2
        if flag: return
        global largest_block_group_info
        cnt, r_cnt, (y, x) = largest_block_group_info
        curr_block_group_info = (block_cnt, rainbow_block_cnt, base_block)
        if cnt < block_cnt: largest_block_group_info = curr_block_group_info
        elif cnt == block_cnt and cnt:
            if r_cnt < rainbow_block_cnt: largest_block_group_info = curr_block_group_info
            elif r_cnt == rainbow_block_cnt:
                if y < base_block[0]: largest_block_group_info = curr_block_group_info
                elif y == base_block[0]:
                    if x < base_block[1]: largest_block_group_info = curr_block_group_info
    # koko
    def fall_proc():
        global board_info
        for j in range(n):
            for k in range(n - 1, 0, -1):
                for i in range(k, n):
                    # Change empty <-> normal block
                    if board_info[i][j] == -2 and board_info[i - 1][j] >= 0:
                        board_info[i][j] = board_info[i - 1][j]
                        board_info[i - 1][j] = -2

    def rotate_proc():
        global board_info
        tmp_board_info = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                tmp_board_info[i][j] = board_info[j][n - 1 - i]
        board_info = tmp_board_info

    def simulation_proc():
        global board_info
        for i in range(n):
            for j in range(n):
                if board_info[i][j] > 0:
                    bfs_proc(board_info[i][j], i, j, False)

        global largest_block_group_info
        cnt, r_cnt, (y, x) = largest_block_group_info
        if cnt < 2: return -1
        #print(largest_block_group_info)
        global point
        point += cnt ** 2
        bfs_proc(board_info[y][x], y, x, True)
        fall_proc()
        rotate_proc()
        fall_proc()
        largest_block_group_info = (0, 0, (-1, -1))

    while True:
        if simulation_proc() == -1: break

    print(point)

solution_proc()
