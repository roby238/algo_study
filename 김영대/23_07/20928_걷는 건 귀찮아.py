import sys
from collections import deque
def solution():
    read = sys.stdin.readline
    n, m = map(int, read().rstrip().split())
    p = [0] + list(map(int, read().rstrip().split()))
    x = [0] + list(map(int, read().rstrip().split()))

    idx = 1
    tmp = 1
    ans = 0
    while(1):
        cnt = p[idx]
        dis = x[idx]
        target = 0
        max = -1

        if m <= cnt + dis:
            print(ans)
            return

        while(idx + tmp <= n and p[idx + tmp] <= cnt + dis):
            if max < p[idx + tmp] + x[idx + tmp] and cnt + dis < p[idx + tmp] + x[idx + tmp]:
                max = p[idx + tmp] + x[idx + tmp]
                target = idx + tmp
            tmp += 1

        if(target):
            idx = target
            tmp = 1
            ans += 1
        else:
            break

    print(-1)


solution()
