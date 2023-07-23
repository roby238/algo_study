import sys
from collections import deque
ans = 1
def solution():
    read = sys.stdin.readline
    N = int(read().rstrip())
    h = []
    t = [0 for _ in range(101)]
    p = [0 for _ in range(N * N)]
    v = [0 for _ in range(N * N)]
    for i in range(N):
        h += list(map(int, read().rstrip().split()))
        for j in range(N):
            t[h[i * N + j]] += 1

    def getParent(x):
        if x == p[x]:
            return x
        p[x] = getParent(p[x])
        return p[x]

    def setParent(a, b):
        pa = getParent(a)
        pb = getParent(b)
        if pa > pb :
            p[pa] = pb
        else:
            p[pb] = pa

    def isValid(s, n):
        return (0 <= n < N * N) and ((s // N == n // N) or (s % N == n % N))

    def bfs(node, height):
        q = deque()
        q.append(node)
        v[node] = 1
        while(len(q) > 0):
            s = q.popleft()
            dn = (1, -N, -1, N)
            for k in range(4):
                n = s + dn[k]
                if not isValid(s, n):
                    continue
                if h[n] > height and v[n] == 0:
                    setParent(s, n)
                    q.append(n)
                    v[n] = 1


    def simulation(height):
        global ans
        for i in range(N * N):
            v[i] = 0
            p[i] = i
        for i in range(N * N):
            if height >= h[i] or v[i] == 1:
                continue
            bfs(i, height)
        cnt = 0
        for i in range(N*N):
            if p[i] == i and h[p[i]] > height:
                cnt += 1
        ans = max(cnt, ans)

    for i in range(1, 101):
        if t[i] == 0: continue
        simulation(i)

    print(ans)

solution()