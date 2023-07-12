import sys
def solution():
    read = sys.stdin.readline
    n, k = map(int, read().rstrip().split())
    A = [0] + list(map(int, read().rstrip().split()))
    B = [0] * (n + 2)
    for i in range(1, n + 1):
        B[i] = A[i - 1] ^ A[i]
    off = 0
    for i in range(1, n - k + 2):
        if B[i]:
            B[i] ^= 1
            B[i + k] ^= 1
            off += 1
    for i in range(n - k + 2, n + 1):
        if B[i]:
            print("Insomnia")
            return
    print(off)

solution()