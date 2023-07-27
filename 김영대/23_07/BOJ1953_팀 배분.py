import sys
def solution():
    read = sys.stdin.readline
    N = int(read().rstrip())
    h = [[]]
    t = [0 for _ in range(N + 1)]
    for _ in range(1, N + 1):
        h.append(list(map(int, read().rstrip().split())))

    def dfs(node, depth):
        if (t[node] != 0): return
        t[node] = (depth % 2) + 1
        for i in range(1, h[node][0] + 1):
            dfs(h[node][i], depth + 1)

    for n in range(1, N + 1):
        dfs(n, 0)

    blue = []
    white = []
    for n in range(1, N + 1):
        if(t[n] == 1):
            blue.append(n)
        elif (t[n] == 2):
            white.append(n)

    print(len(blue))
    for n in blue:
        print(n, end = " ")
    print()
    print(len(white))
    for n in white:
        print(n, end = " ")

solution()

