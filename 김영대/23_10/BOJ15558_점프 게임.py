import sys
from collections import deque
def solution():
    read = sys.stdin.readline
    n, k = map(int, read().split())
    line = []
    line.append(read().rstrip())
    line.append(read().rstrip())
    visit = [[False for _ in range(n)] for _ in range(2)]
    q = deque()

    def jumpProc(lineInfo, step, sec, state):
        # jump
        if not state:
            nextNode = (not lineInfo, step + k, sec + 1)
            if nextNode[1] >= n: return True
        # go
        elif state == 1:
            nextNode = (lineInfo, step + 1, sec + 1)
            if nextNode[1] >= n: return True
        # back
        else:
            nextNode = (lineInfo, step - 1, sec + 1)

        # step >= sec 가려는 step이 sec보다 크거나 같으면 step이 사라지지 않았으므로 갈 수 있음
        if nextNode[1] >= nextNode[2]:
            # 안전한 공간이고 방문한 적 없으면
            if line[nextNode[0]][nextNode[1]] == '1' and not visit[nextNode[0]][nextNode[1]]:
                q.append(nextNode) # push to queue
                visit[nextNode[0]][nextNode[1]] = True # visit 처리

        return False

    def bfsProc():
        q.append((0, 0, 0))
        while q:
            currNode = q.popleft()
            if currNode[2] >= n: break
            # jump
            if jumpProc(currNode[0], currNode[1], currNode[2], 0): return True
            # go
            if jumpProc(currNode[0], currNode[1], currNode[2], 1): return True
            # back
            jumpProc(currNode[0], currNode[1], currNode[2], 2) # 뒤로만 가는 거니까 게임 끝낼 여지 없음

        return False

    # 끝낼 수 있으면 1
    if bfsProc(): print(1)
    # 아니면 0
    else: print(0)

solution()