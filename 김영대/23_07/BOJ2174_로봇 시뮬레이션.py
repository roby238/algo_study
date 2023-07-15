import sys

def solution():
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    read = sys.stdin.readline
    A, B = map(int, read().rstrip().split())
    N, M = map(int, read().rstrip().split())

    m = [[0 for _ in range(A + 2)] for __ in range(B + 2)]
    robot = [0]
    command = [0]
    for i in range(B + 2):
        for j in range(A + 2):
            if 0 < j < A + 1 and 0 < i < B + 1:
                m[i][j] = 0
            else:
                m[i][j] = -1

    for i in range(1, N+1):
        x, y, c = read().rstrip().split()
        if c == 'N':
            d = 0
        elif c == 'E':
            d = 1
        elif c == 'S':
            d = 2
        else:
            d = 3
        robot.append( [B + 1 - int(y), int(x), d] )
        m[B + 1 - int(y)][int(x)] = i

    for _ in range(1, M+1):
        n, c, r = read().rstrip().split()
        command.append( [int(n), c, int(r)] )

    for i in range(1, M+1):
        n = command[i][0]
        c = command[i][1]

        if c != 'F':
            command[i][2] %= 4
        for j in range(1, command[i][2]+1):
            if c == 'R':
                robot[n][2] = (robot[n][2] + 1) % 4
            elif c == 'L':
                robot[n][2] = (robot[n][2] - 1) % 4
            else:
                m[robot[n][0]][robot[n][1]] = 0

                if robot[n][2] % 2 == 0:
                    robot[n][0] += dy[robot[n][2]]
                else:
                    robot[n][1] += dx[robot[n][2]]

                if m[robot[n][0]][robot[n][1]] == -1:
                    print("Robot", n, "crashes into the wall")
                    return
                elif m[robot[n][0]][robot[n][1]] > 0:
                    print("Robot", n, "crashes into robot", m[robot[n][0]][robot[n][1]])
                    return
                m[robot[n][0]][robot[n][1]] = n
    print("OK")

solution()