import sys
def solution():
    read = sys.stdin.readline
    n, m = map(int, read().split())
    lct = list(map(int, read().rstrip().split()))

    def search():
        lctMax = max(lct)
        lo = 0; hi = 1000000000
        while(lo <= hi):
            mid = (lo + hi) // 2
            if mid < lctMax:
                lo = mid + 1
            else:
                subSum = 0; cnt = 1
                for i in range(n):
                    if mid < subSum + lct[i]:
                        subSum = 0
                        cnt += 1
                    subSum += lct[i]
                if m < cnt:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return lo

    print(search())

solution()