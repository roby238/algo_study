import sys
def solution():
    read = sys.stdin.readline
    n = int(read())
    pmt = list(map(int, read().split()))
    numPtr = 0
    for i in range(n - 1):
        if pmt[i] < pmt[i + 1]: numPtr = i + 1
    if not numPtr: print(-1)
    else:
        target = pmt[numPtr - 1]
        minVal = n
        minValPtr = n
        for i in range(numPtr, n):
            if target < pmt[i]:
                minVal = min(minVal, pmt[i])
                minValPtr = i
        tmp = pmt[numPtr - 1]
        pmt[numPtr - 1] = pmt[minValPtr]
        pmt[minValPtr] = tmp
        partPmt = pmt[numPtr:]
        partPmt.sort()
        for i in range(numPtr):
            print(f"{pmt[i]}", end = " ")
        for i in range(len(partPmt)):
            print(f"{partPmt[i]}", end=" ")
solution()