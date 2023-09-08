A, B = map(int, input().split())
N, M = map(int, input().split())
location = [[0] * (A + 1) for _ in range(B + 1)]
dir_x, dir_y = [0, 1, 0, -1], [1, 0, -1, 0]
y, x, r_dir = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)
command = []

def move(idx, nx, ny):
    location[y[idx]][x[idx]] = 0
    location[ny][nx] = idx
    y[idx], x[idx] = ny, nx

for i in range(1, N + 1):
    x[i], y[i], direction = map(str, input().split())
    x[i], y[i] = int(x[i]), int(y[i])
    location[y[i]][x[i]] = i
    r_dir[i] = {'N': 0, 'E': 1, 'S': 2, 'W': 3}[direction]

for _ in range(M):
    a, b, c = input().split()
    command.append((int(a), b, int(c)))

for idx, com, num in command:
    if com == 'L':
        num %= 4
        r_dir[idx] = (r_dir[idx] - num) % 4
        
    elif com == 'R':
        r_dir[idx] = (r_dir[idx] + num) % 4
        
    elif com == 'F':
        for _ in range(num):
            nx = x[idx] + dir_x[r_dir[idx]]
            ny = y[idx] + dir_y[r_dir[idx]]
            
            if not (1 <= ny <= B and 1 <= nx <= A):
                print("Robot", idx, "crashes into the wall")
                exit()
                
            elif location[ny][nx]:
                print("Robot", idx, "crashes into robot", location[ny][nx])
                exit()

            move(idx, nx, ny)

print("OK")