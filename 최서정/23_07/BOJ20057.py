n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]
x, y = n // 2, n // 2
dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

wind_x = (
    (-1, 1, -2, 2, 0, -1, 1, -1, 1),
    (-1, -1, 0, 0, 2, 0, 0, 1, 1),
    (1, -1, 2, -2, 0, 1, -1, 1, -1),
    (1, 1, 0, 0, -2, 0, 0, -1, -1)
)
wind_y = (
    (1, 1, 0, 0, -2, 0, 0, -1, -1),
    (-1, 1, -2, 2, 0, -1, 1, -1, 1),
    (-1, -1, 0, 0, 2, 0, 0, 1, 1),
    (1, -1, 2, -2, 0, 1, -1, 1, -1)
)

rate = (1, 1, 2, 2, 5, 7, 7, 10, 10)

def wind(x, y, dir) :
    value = 0
    sand = d[x][y]
    sum_value = 0
    for i in range(9) :
        nx = x + wind_x[dir][i]
        ny = y + wind_y[dir][i]
        wind_sand = (sand * rate[i]) // 100
        sum_value += wind_sand

        if not (0 <= nx < n and 0 <= ny < n) :
            value += wind_sand
            continue
        d[nx][ny] += wind_sand

    nx = x + dx[dir]
    ny = y + dy[dir]
    a = sand - sum_value
    if not (0 <= nx < n and 0 <= ny < n) :
        value += a
    else :
        d[nx][ny] += a
    d[x][y] = 0
    return value

def solve(x, y) :
    value = 0
    visited = [[False] * n for _ in range(n)]
    dir = -1
    while True :
        if x == 0 and y == 0 :
            break
        visited[x][y] = True
        nd = (dir + 1) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]

        if visited[nx][ny] :
            nd = dir
            nx = x + dx[nd]
            ny = y + dy[nd]
        value += wind(nx, ny, nd)
        x, y, dir = nx, ny, nd

    return value


result = solve(x, y)

print(result)
