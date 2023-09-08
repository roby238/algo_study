import sys
from functools import cmp_to_key
students = [0 for _ in range(101)]
def cmp(a, b):
    if students[a[0]] == students[b[0]]:
        if a[1] < b[1]:
            return 1
        else:
            return -1
    if students[a[0]] < students[b[0]]:
        return 1
    else:
        return -1
def solution():
    read = sys.stdin.readline
    N = int(read().strip())
    R = int(read().strip())

    candidates = []

    sIdx = list(map(int, read().rstrip().split()))
    for i in range(R):
        if len(candidates) < N:
            if students[sIdx[i]] == 0:
                candidates.append((sIdx[i], i))
            students[sIdx[i]] += 1
        elif len(candidates) == N:
            if students[sIdx[i]] == 0:
                trash = candidates.pop()
                students[trash[0]] = 0
                candidates.append((sIdx[i], i))
            students[sIdx[i]] += 1

        candidates.sort(key=cmp_to_key(cmp))

    candidates.sort(key=lambda x: x[0])

    answer = ""
    for i in range(0, len(candidates)):
        answer += str(candidates[i][0]) + " "
    print(answer)

solution()