import sys
from collections import deque


def solution_proc():
    read = sys.stdin.readline
    r, c = 12, 6
    field = [list(read().rstrip()) for _ in range(r)]
    dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)

    def swap_block(y1, x1, y2, x2):
        tmp = field[y1][x1]
        field[y1][x1] = field[y2][x2]
        field[y2][x2] = tmp

    def apply_gravity():
        for j in range(c):
            for i in range(1, r):
                tmp_i = i
                while 1:
                    if tmp_i < 1: break
                    if field[tmp_i][j] == '.' and field[tmp_i - 1][j] != '.':
                        swap_block(tmp_i, j, tmp_i - 1, j)
                    else: break
                    tmp_i -= 1

    def pop_groups(groups):
        for group in groups:
            for pos in group:
                field[pos[0]][pos[1]] = '.'

        return 0

    def bfs(y, x, c, is_visited):
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

    def check_possible_to_pop():
        is_visited = [[0 for _ in range(6)] for _ in range(12)]
        groups = list()
        for i in range(r):
            for j in range(c):
                if field[i][j] == '.': continue
                group = bfs(i, j, field[i][j], is_visited)
                if len(group) >= 4: groups.append(group)

        return groups

    def simulation():
        turn_cnt = 0
        while 1:
            groups = check_possible_to_pop()
            if not len(groups): break
            pop_groups(groups)
            apply_gravity()
            turn_cnt += 1

        return turn_cnt

    print(simulation())


solution_proc()
