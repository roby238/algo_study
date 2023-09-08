import sys
from collections import deque

def solution():
    read = sys.stdin.readline
    N, L, R = map(int, read().split())
    people = [list(map(int, read().split())) for _ in range(N)]
    days = [[0 for _ in range(N)] for _ in range(N)]

    dy = (1, -1, 0, 0)
    dx = (0, 0, 1, -1)
    day = 1
    moveFlag = True
    while moveFlag:
        moveFlag = False
        for i in range(N):
            for j in range(N):
                if days[i][j] == day: continue

                uni = [(i, j)]
                q = deque()
                q.append((i, j))
                days[i][j] = day
                peopleSum = people[i][j]
                while len(q) > 0:
                    sy, sx = q.popleft()
                    for k in range(4):
                        ny, nx = sy + dy[k], sx + dx[k]
                        if N <= ny or 0 > ny or N <= nx or 0 > nx or days[ny][nx] == day: continue
                        if abs(people[ny][nx] - people[sy][sx]) > R or \
                                abs(people[ny][nx] - people[sy][sx]) < L: continue
                        uni.append((ny, nx))
                        peopleSum += people[ny][nx]
                        q.append((ny, nx))
                        days[ny][nx] = day
                        moveFlag = True
                for nation in uni:
                    people[nation[0]][nation[1]] = peopleSum // len(uni)
        day += 1

    print(day - 2)

solution()

