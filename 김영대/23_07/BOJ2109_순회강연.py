import sys
def solution():
    read = sys.stdin.readline
    N = int(read().rstrip())
    schedule = []
    visited = [0 for _ in range(10001)]
    for i in range(N):
        schedule.append(list(map(int, read().rstrip().split())))

    if len(schedule) > 0:
        schedule.sort(key = lambda x: -x[0])

    ans = 0
    for i in range(N):
        for j in range(schedule[i][1], 0, -1):
            if not visited[j]:
                visited[j] = 1
                ans += schedule[i][0]
                break;

    print(ans)
solution()