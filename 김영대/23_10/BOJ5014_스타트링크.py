import sys
from collections import deque
def solutionProc():
    read = sys.stdin.readline
    f, s, g, u, d = map(int, read().split())
    visit = [False for _ in range(f + 1)]
    q = deque()
    q.append((s, 0))
    possibleFlag = False
    minCnt = float("inf")

    if (not d and g < s) or (not u and g > s):
        print("use the stairs")
        return

    while q:
        curr, cnt = q.popleft()
        if curr == g:
            minCnt = cnt
            possibleFlag = True
            break

        if curr + u <= f and not visit[curr + u]:
            q.append((curr + u, cnt + 1))
            visit[curr + u] = True
        if curr - d > 0 and not visit[curr - d]:
            q.append((curr - d, cnt + 1))
            visit[curr - d] = True

    if possibleFlag:
        print(minCnt)
    else:
        print("use the stairs")

solutionProc()