import sys
import heapq
def solution():
    read = sys.stdin.readline
    N = int(read())
    q = []
    for i in range(N):
        for j in map(int, read().rstrip().split()):
            if len(q) < N:
                heapq.heappush(q, j)
            elif q[0] < j:
                heapq.heappush(q, j)
                heapq.heappop(q)
    print(heapq.heappop(q))

solution()