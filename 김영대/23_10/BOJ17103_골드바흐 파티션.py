import sys
def solution():
    read = sys.stdin.readline
    n = int(read())
    isNotPrime = [0 for _ in range(1000001)]

    def setPrimeProc():
        for i in range(3, 1000001, 2):
            if not isNotPrime[i]:
                j = 3
                while i * j <= 1000000:
                    isNotPrime[i * j] = 1
                    j += 2

    setPrimeProc()

    def subNumProc(num):
        if num == 4:
            print(1)
            return
        cnt = 0
        for i in range(3, num // 2 + 1, 2):
            if not isNotPrime[i] and not isNotPrime[num - i]:
                cnt += 1
        print(cnt)

    for _ in range(n):
        num = int(read())
        subNumProc(num)

solution()