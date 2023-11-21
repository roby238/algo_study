import sys
import copy
from collections import deque
min_spread_time = float("inf")
def solution_proc():
    read = sys.stdin.readline
    n, m = map(int, read().split())
    room_info = []
    virus_pos = []
    empty_cnt = -m
    for i in range(n):
        room_info.append(list(map(int, read().split())))
        for j in range(n):
            if room_info[i][j] != 1:
                empty_cnt += 1
            if room_info[i][j] == 2:
                room_info[i][j] = 0
                virus_pos.append((i, j))
    dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)
    #print(room_info)
    #print(empty_cnt)
    def is_valid(y, x):
        if y < 0 or y >= n or x < 0 or x >= n: return False
        return True
    def bfs_proc(idx, tmp_room_info, tmp_empty_cnt):
        queue = deque()
        spread_time = 0
        for i in idx:
            y, x = virus_pos[i]
            tmp_room_info[y][x] = 2
            #tmp_empty_cnt -= 1
            queue.append((y, x, 0))
        #print(queue)
        while queue:
            sy, sx, t = queue.popleft()
            #print(sy, sx, t)
            spread_time = max(spread_time, t)
            for k in range(4):
                ny, nx = sy + dy[k], sx + dx[k]
                if not is_valid(ny, nx): continue
                if not tmp_room_info[ny][nx]:
                    tmp_room_info[ny][nx] = 2
                    tmp_empty_cnt -= 1
                    queue.append((ny, nx, t + 1))
        #print(tmp_empty_cnt)
        #print(tmp_room_info)
        global min_spread_time
        if not tmp_empty_cnt:
            min_spread_time = min(min_spread_time, spread_time)

    comb = deque()
    def combination(index, depth):
        if depth == m:
            #print(comb)
            bfs_proc(comb, copy.deepcopy(room_info), empty_cnt)
            return
        for i in range(index, len(virus_pos)):
            comb.append(i)
            combination(i + 1, depth + 1)
            comb.pop()

    combination(0, 0)

    if min_spread_time == float("inf"):
        print(-1)
    else:
        print(min_spread_time)

solution_proc()