import sys
from collections import deque


def solution_proc():
    """
    Get key count when only ONE coin fall.
    :return:
    """
    # Get inputs and set variables.
    read = sys.stdin.readline
    n, m = map(int, read().split())
    coin_pos = []
    board_status = []
    for i in range(n):
        board_status.append(read().rstrip())
        for j in range(m):
            if board_status[i][j] == 'o':
                coin_pos.append((i, j))
    # Visit list
    visit = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
    # Direction vectors
    dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)

    def is_valid(y, x):
        """
        Determine that it is valid position.
        :param y: coordinate y
        :param x: coordinate x
        :return: true or false
        """
        return 0 <= y < n and 0 <= x < m

    def face_wall(cy, cx, ny, nx, f_cnt):
        """
        When the coin face wall, change position or stay.
        :param cy: current coordinate y
        :param cx: current coordinate x
        :param ny: next coordinate y
        :param nx: next coordinate x
        :param f_cnt: fall count(maximum two)
        :return: ny, nx, f_cnt
        """
        if is_valid(ny, nx):
            if board_status[ny][nx] == '#':
                ny, nx = cy, cx
        else: f_cnt += 1

        return ny, nx, f_cnt

    def bfs_proc():
        """
        BFS gets key count regarding position of two coins.
        :return: key count or -1(10 and over)
        """
        # An empty queue
        queue = deque()
        queue.append((coin_pos[0][0], coin_pos[0][1], \
                      coin_pos[1][0], coin_pos[1][1], 0))
        # While queue is alive...
        while queue:
            # Dequeue
            cy1, cx1, cy2, cx2, cnt = queue.popleft()
            if cnt >= 10: return -1
            # Process of four direction
            for k in range(4):
                # Next position of each coin.
                ny1, nx1 = cy1 + dy[k], cx1 + dx[k]
                ny2, nx2 = cy2 + dy[k], cx2 + dx[k]
                # Generate fall count
                fall_cnt = 0
                # Calculate fall count if face wall or not.
                ny1, nx1, fall_cnt = face_wall(cy1, cx1, ny1, nx1, fall_cnt)
                ny2, nx2, fall_cnt = face_wall(cy2, cx2, ny2, nx2, fall_cnt)
                # If fall count is zero, enqueue positions and key count.
                if not fall_cnt:
                    if visit[ny1][nx1][ny2][nx2]: continue
                    visit[ny1][nx1][ny2][nx2] = 1
                    queue.append((ny1, nx1, ny2, nx2, cnt + 1))
                # Else if fall count is one, increase key count and return it.
                elif fall_cnt == 1: return cnt + 1
        # Default result when it is nothing to move.
        return -1
    # Print answer.
    print(bfs_proc())


solution_proc()
