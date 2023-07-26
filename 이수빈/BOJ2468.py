from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
max_height = 0
safe_count = 0
mp_height = []
for _ in range(N):
    mp_height.append(list(map(int, input().split())))

def bfs(x, y, height, check):
    q = deque([(x, y)])
    check[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]      
            if 0 <= nx < N and 0 <= ny < N and not check[nx][ny] and mp_height[nx][ny] > height:
                check[nx][ny] = 1
                q.append((nx, ny))

for h in mp_height:
    max_height = max(max_height, max(h))

for height in range(max_height + 1):
    check = [[False] * N for _ in range(N)]
    safe = 0
    for x in range(N):
        for y in range(N):
            if not check[x][y] and mp_height[x][y] > height:
                bfs(x, y, height, check)
                safe += 1

    safe_count = max(safe_count, safe)

print(safe_count)