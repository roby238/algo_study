import sys
from collections import deque
def solution():
    read = sys.stdin.readline
    N, M = map(int, read().rstrip().split())
    c = []
    for _ in range(N):
        c.append(list(map(int, read().rstrip().split())))
    v = [[0 for _ in range(M)] for __ in range(N)]
    di = (0, 0, 1, -1)
    dj = (1, -1, 0, 0)
    pq = deque() # line 검사 큐
    nq = deque() # marginal 치즈 검사 큐

    def isInvalid(p):
        if (p[0] < 0) or (p[1] < 0) or (p[0] >= N) or (p[1] >= M):
            return True
        return False

    def lineDetect():
        while(len(pq) > 0):
            s = pq.popleft()
            for k in range(4):
                n = (s[0] + di[k], s[1] + dj[k])
                # 범위 검사
                if(isInvalid(n)):
                    continue
                # 처음 보는 외부 공기
                if (not c[n[0]][n[1]]) and (not v[n[0]][n[1]]):
                    pq.append(n)
                    v[n[0]][n[1]] = 1
                # 치즈 발견
                elif c[n[0]][n[1]] == 1:
                    nq.append(n)

    def meltDown():
        while(len(nq) > 0):
            s = nq.popleft()
            meltCount = 0
            for k in range(4):
                n = (s[0] + di[k], s[1] + dj[k])
                # 범위 검사
                if (isInvalid(n)):
                    continue
                # 외부 공기 -> 다시 라인 디텍션으로
                if (not c[n[0]][n[1]]) and (v[n[0]][n[1]]):
                    meltCount += 1
                    pq.append(n)
            # 두 면 이상 공기와 접촉 -> 여기서 pq에 추가하면 메모리 초과
            if meltCount >= 2:
                c[s[0]][s[1]] = 0
    # 시간 계산
    hour = 0
    pq.append((0, 0)) # 초기 외부 공기의 시작 지점
    while(1):
        lineDetect() # 공기-치즈 라인 검사
        if len(nq) == 0:
            break
        meltDown() # 산화된 치즈
        hour += 1

    print(hour)

solution()