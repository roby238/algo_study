def solution():
    R = input()
    C = input()
    jnq = [], jpq = [], fnq = [], fpq = []
    m = [[0 for j in range(C + 2)] for i in range(R + 2)]
    v = [[0 for j in range(C + 2)] for i in range(R + 2)]
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            c = input()
            m[i][j] = c
            if c == 'J':
                jnq.append([i, j])
            elif c == 'F':
                fnq.append([i, j])

    def isValid(i, j):
        return (i >= 0 and i <= R + 1 and j >= 0 and j <= C + 1 and m[i][j] != '#')

    def bfs():
        escapeTime = 1
        di = (1, -1, 0, 0)
        dj = (0, 0, 1, -1)
        while jnq.size() > 0:
            fpq = fnq
            fnq = []
            while fpq.size > 0:
                s = fpq.front()
                fpq.pop()
                for k in range(0, 4):
                    n = s + [di[k], dj[k]]
                    if ~isValid(n[0], n[1]):
                        continue
                    if m[n[0]][n[1]] == '.':
                        fnq.push(n);
                        m[n[0]][n[1]] = '#'
            jpq = jnq
            jnq = []
            while jpq.size > 0:
                s = jpq.front()
                jpq.pop()
                for k in range(0, 4):
                    n = s + [di[k], dj[k]]
                    if ~isValid(n[0], n[1]):
                        continue
                    if m[n[0]][n[1]] == '.' and v[n[0]][n[1]] == 0:
                        jnq.push(n)
                        m[n[0]][n[1]] = 'J'
                        v[n[0]][n[1]] = 1
                    elif m[n[0]][n[1]] == 0:
                        return escapeTime
            escapeTime += 1

    result = bfs()

    if result > 0:
        print(result)
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    solution()