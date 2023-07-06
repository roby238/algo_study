# BOJ_4179
# 불!

from collections import deque

# 미로
maze = list()
# 초기 시간
time = 0
# 지훈 queue // 위치 정보 좌표 2개, 시간 정보 1개
j_queue = deque()
# 불 queue // 위치 정보 좌표 2개
f_queue = deque()

move_list = [(-1, 0), (1, 0),  # y축 이동
             (0, -1), (0, 1)]  # x축 이동

# R, C 입력 받기
row, col = map(int, input().split())

# 미로 정보 입력 받기, 지훈이와 불의 초기 위치 입력
for i in range(row):
    maze.append(input())
    for j in range(col):
        if maze[i][j] == 'J':
            j_queue.append((i, j, time))
        if maze[i][j] == 'F':
            f_queue.append((i, j))

while j_queue:
    for _ in range(len(f_queue)):
        fx, fy = f_queue.popleft()
        # 불 이동 및 f_queue에 추가
        for dx, dy in move_list:
            nx, ny = fx + dx, fy + dy
            if 0 <= nx < row and 0 <= ny < col and (maze[nx][ny] == '.' or maze[nx][ny] == 'J'):
                maze[nx] = maze[nx][:ny] + 'F' + maze[nx][ny+1:]
                f_queue.append((nx, ny))

    for _ in range(len(j_queue)):
        jx, jy, time = j_queue.popleft()
        # 탈출 성공하면, 시간 출력하고 종료
        if jx == 0 or jx == row - 1 or jy == 0 or jy == col - 1:
            print(time + 1)
            exit()
        # 지훈 이동 및 j_queue에 추가
        for dx, dy in move_list:
            nx, ny = jx + dx, jy + dy
            if 0 <= nx < row and 0 <= ny < col and maze[nx][ny] == '.':
                maze[nx] = maze[nx][:ny] + 'J' + maze[nx][ny+1:]
                j_queue.append((nx, ny, time + 1))

# if not j_queue:
print("IMPOSSIBLE")
