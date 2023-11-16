import sys
from collections import deque
ans = float("inf")
def solution_proc():
    read = sys.stdin.readline
    m, n = map(int, read().split())
    route_info = [list(map(int, read().split())) for _ in range(m)]
    start_info = list(map(int, read().split()))
    end_info = list(map(int, read().split()))
    dy, dx = (0, 0, 1, -1), (1, -1, 0, 0)
    dir_mapping = ((0, 2, 1, 1), (2, 0, 1, 1), (1, 1, 0, 2), (1, 1, 2, 0))
    visit = [[[float("inf") for _ in range(4)] for _ in range(n)] for _ in range(m)]
    def is_valid(y, x):
        if y >= m or y < 0 or x >= n or x < 0: return False
        return True

    def bfs_proc():
        queue = deque()
        queue.append((start_info[:2], start_info[2], 0))
        visit[start_info[0] - 1][start_info[1] - 1][start_info[2] - 1] = 0
        while queue:
            s_pos, s_dir, s_cnt = queue.popleft()
            [sy, sx] = s_pos
            s_dir -= 1
            if sy == end_info[0] and sx == end_info[1]:
                visit[sy - 1][sx - 1][end_info[2] - 1] = min(visit[sy - 1][sx - 1][end_info[2] - 1],
                                                             s_cnt + dir_mapping[s_dir][end_info[2] - 1])
            sy -= 1
            sx -= 1
            for k in range(4):
                for l in range(1, 4):
                    ny, nx = sy + dy[k] * l, sx + dx[k] * l
                    if not is_valid(ny, nx): break
                    if route_info[ny][nx]: break
                    n_cnt = s_cnt + dir_mapping[s_dir][k] + 1
                    if n_cnt >= visit[ny][nx][k]: continue
                    visit[ny][nx][k] = n_cnt
                    queue.append(([ny + 1, nx + 1], (k + 1) % 4, n_cnt))

    bfs_proc()
    print(visit[end_info[0] - 1][end_info[1] - 1][end_info[2] - 1])


solution_proc()
