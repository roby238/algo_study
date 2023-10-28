import sys

def solutionProc():
    read = sys.stdin.readline
    m, n = map(int, read().split())

    s = [1 for _ in range(2 * m - 1)]
    for _ in range(n):
        zero, one, two = map(int, read().split())
        for j in range(0, one):
            s[zero + j] += 1
        for j in range(0, two):
            s[zero + one + j] += 2

    for j in range(m - 1, 2 * m - 1):
        print(s[j], end=" ")
    print()
    for i in range(1, m):
        print(s[m - 1 - i], end=" ")
        for j in range(m, 2 * m - 1):
            print(s[j], end=" ")
        print()


solutionProc()
