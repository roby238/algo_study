import sys
global maxRes, minRes
maxRes, minRes = -1 * float("inf"), float("inf")
def solutionProc():
    read = sys.stdin.readline
    n = int(read())
    a = list(map(int, read().split()))
    op = list(map(int, read().split()))

    def dfs(d, res):
        if d == n :
            global maxRes, minRes
            maxRes = max(maxRes, res)
            minRes = min(minRes, res)
            return 1

        if op[0]:
            op[0] -= 1
            dfs(d + 1, res + a[d])
            op[0] += 1
        if op[1]:
            op[1] -= 1
            dfs(d + 1, res - a[d])
            op[1] += 1
        if op[2]:
            op[2] -= 1
            dfs(d + 1, res * a[d])
            op[2] += 1
        if op[3]:
            op[3] -= 1
            if res < 0:
                dfs(d + 1, -(abs(res) // a[d]))
            else:
                dfs(d + 1, res // a[d])
            op[3] += 1

    dfs(1, a[0])
    global maxRes, minRes
    print(maxRes, minRes)

solutionProc()