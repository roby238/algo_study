import sys
def solution():
    read = sys.stdin.readline
    testCase = 1
    p = []

    def getParent(x):
        if x == p[x]: return x
        p[x] = getParent(p[x])
        return p[x]

    def setParent(a, b):
        pa, pb = getParent(a), getParent(b)
        if pa == pb: p[pa] = 0
        elif pa > pb: p[pa] = pb
        else: p[pb] = pa

    while 1:
        n, m = map(int, read().split())
        p = [i for i in range(n+1)]
        if not n and not m: break

        for _ in range(m):
            a, b = map(int, read().split())
            setParent(a, b)

        tree = 0
        for i in range(1, n + 1):
            if p[i] == i:
                tree += 1

        if tree > 1:
            print("Case", testCase, end = "")
            print(": A forest of", tree, "trees.")
        elif tree:
            print("Case", testCase, end = "")
            print(": There is one tree.")
        else:
            print("Case", testCase, end = "")
            print(": No trees.")
        testCase += 1

solution()