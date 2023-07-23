import sys
from collections import deque
ans = 1001
def solution():
    read = sys.stdin.readline
    N = int(read().rstrip())
    popula = [0] + list(map(int, read().rstrip().split()))
    node = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    team = ['b' for _ in range(N + 1)]
    visit = [0 for _ in range(N + 1)]

    for i in range(1, N + 1):
        row = list(map(int,read().rstrip().split()))
        for j in range(1, row[0] + 1):
            node[i][row[j]] = 1
            node[row[j]][i] = 1

    def bfs(l, t):
        for i in range(1, N + 1): visit[i] = False
        visit[l[0]] = True
        q = deque()
        q.append(l[0])
        count = 0
        while(len(q) > 0):
            s = q.popleft()
            count += 1
            for i in range(1, N + 1):
                if ((team[i] != t) or (visit[i]) or (not node[s][i])):
                    continue
                visit[i] = True
                q.append(i)
        if len(l) == count:
            return True
        return False

    def isValid():
        a = []
        b = []
        for i in range(1, N + 1):
            if team[i] == 'a':
                a.append(i)
            else:
                b.append(i)
        if (not bfs(a, 'a') or not bfs(b, 'b')): return False

        return True

    def dfs(target, depth):
        global ans
        if depth == N: return

        if depth > 0 and isValid():
            pa = 0
            pb = 0
            for i in range(1, N + 1):
                if team[i] == 'a': pa += popula[i]
                else: pb += popula[i]
            ans = min(ans, abs(pa - pb))

        for i in range(target, N + 1):
            if team[i] == 'a': continue
            team[i] = 'a'
            dfs(i, depth + 1)
            team[i] = 'b'

    dfs(1, 0)

    global ans
    if(ans == 1001):
        ans = -1
    print(ans)

solution()