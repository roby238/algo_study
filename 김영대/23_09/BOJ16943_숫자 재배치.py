import sys
c = -1
def solution():
    read = sys.stdin.readline
    line = read()
    a = line.split()[0]
    b = int(line.split()[1])
    used = [0 for _ in range(len(a))]
    def dfs(d, n):
        if d == len(a):
            if n >= b:
                return
            else:
                global c
                c = max(c, n)
                return
        for i in range(len(a)):
            if used[i]: continue
            if d == 0 and a[i] == '0': continue
            used[i] = 1
            dfs(d + 1, n * 10 + int(a[i]))
            used[i] = 0

    dfs(0, 0)

    print(c)

solution()