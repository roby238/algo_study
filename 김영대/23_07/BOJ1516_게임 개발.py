import sys
from collections import deque

def solution():
    read = sys.stdin.readline
    n = int(read())
    buildings = [[] for _ in range(n + 1)]
    buildTime = [0 for _ in range(n + 1)]
    topology = [0 for _ in range(n + 1)]
    buildTimeSum = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        row = list(map(int, read().split()))
        buildTime[i] = row[0]
        topology[i] = len(row) - 2
        for j in row[1:-1]:
            buildings[j].append(i)

    def tSort():
        q = deque()
        
        for i in range(1, n + 1):
            if topology[i] == 0:
                q.append(i)
                buildTimeSum[i] = buildTime[i]
                
        while(len(q) > 0):
            currentNode = q.popleft()
            for nextNode in buildings[currentNode]:
                topology[nextNode] -= 1
                if topology[nextNode] == 0:
                    q.append(nextNode)
                buildTimeSum[nextNode] = max(buildTimeSum[nextNode], buildTime[nextNode] + buildTimeSum[currentNode])
        
    tSort()

    for i in range(1, n + 1): 
            print(buildTimeSum[i])

solution()