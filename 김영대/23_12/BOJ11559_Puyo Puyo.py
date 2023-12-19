import sys
from collections import deque

def solution_proc():
    read = sys.stdin.readline
    r, c = 12, 6
    field = [list(read().rstrip()) for _ in range(r)]
    is_visited = [[0 for _ in range(6)] for _ in range(12)]
    dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)

    def swap(y1, x1, y2, x2):
        tmp = field[y1][x1]
        field[y1][x1] = field[y2][x2]
        field[y2][x2] = tmp

    def applying_gravity_proc():
        for j in range(c):
            for i in range(r - 1, -1, -1):
                tmp_i = i
                while 1:
                    if field[tmp_i][j] != '.' and tmp_i < 11:
                        if field[tmp_i + 1][j] == '.':
                            swap(i, j, tmp_i + 1, j)
                            tmp_i += 1
                        else: break
                    else: break

    def pop_proc(groups):
        for group in groups:
            for pos in group:
                field[pos[0]][pos[1]] = '.'

        return 0

    def bfs_proc(y, x, c):
        queue = deque()
        queue.append((y, x))
        is_visited[y][x] = 1
        group = list()
        group.append((y, x))
        while queue:
            cy, cx = queue.popleft()
            for k in range(4):
                ny, nx = cy + dy[k], cx + dx[k]
                if not (0 <= ny < 12 and 0 <= nx < 6): continue
                if is_visited[ny][nx]: continue
                if c != field[ny][nx]: continue
                is_visited[ny][nx] = 1
                group.append((ny, nx))
                queue.append((ny, nx))

        return group

    def check_pop_proc():
        groups = list()
        for i in range(r):
            for j in range(c):
                if field[i][j] == '.': continue
                group = bfs_proc(i, j, field[i][j])
                if len(group) >= 4: groups.append(group)

        return groups

    def simulation_proc():
        turn_cnt = 0
        while 1:
            groups = check_pop_proc()
            if not len(groups): break
            pop_proc(groups)
            applying_gravity_proc()
            turn_cnt += 1
            for row in field:
                print(row)

        return turn_cnt

    print(simulation_proc())


solution_proc()
