import sys


def solution():
    inp = sys.stdin.readline
    R, C = map(int, inp().split())
    jnq = []
    fnq = []
    m = [[0 for _ in range(C + 2)] for _ in range(R + 2)]
    v = [[0 for _ in range(C + 2)] for _ in range(R + 2)]

    m[0] = ['0'] * (C + 2)
    m[R + 1] = ['0'] * (C + 2)
    for i in range(1, R + 1):
        row = inp().rstrip()
        row = '0' + row + '0'
        for j in range(0, C + 2):
            m[i][j] = row[j]
            if m[i][j] == 'J':
                jnq.append([i, j])
            elif m[i][j] == 'F':
                fnq.append([i, j])

    def bfs(jnq, fnq):
        escapeTime = 1
        di = (1, -1, 0, 0)
        dj = (0, 0, 1, -1)
        while len(jnq) > 0:
            fpq = fnq
            fnq = []
            while len(fpq) > 0:
                s = fpq.pop(0)
                for k in range(0, 4):
                    ni = s[0] + di[k]
                    nj = s[1] + dj[k]

                    if not ((ni >= 0) and (ni <= R + 1) and (nj >= 0) and (nj <= C + 1) and (m[ni][nj] != '#')):
                        continue

                    if m[ni][nj] == '.':
                        fnq.append([ni, nj])
                        m[ni][nj] = '#'
            jpq = jnq
            jnq = []
            while len(jpq) > 0:
                s = jpq.pop(0)
                for k in range(0, 4):
                    ni = s[0] + di[k]
                    nj = s[1] + dj[k]

                    if not ((ni >= 0) and (ni <= R + 1) and (nj >= 0) and (nj <= C + 1) and (m[ni][nj] != '#')):
                        continue

                    if m[ni][nj] == '.' and v[ni][nj] == 0:
                        jnq.append([ni, nj])
                        m[ni][nj] = 'J'
                        v[ni][nj] = 1
                    elif m[ni][nj] == '0':
                        return escapeTime
            escapeTime += 1
        return 0

    result = bfs(jnq, fnq)

    if result > 0:
        print(result)
    else:
        print("IMPOSSIBLE")


if __name__ == '__main__':
    solution()