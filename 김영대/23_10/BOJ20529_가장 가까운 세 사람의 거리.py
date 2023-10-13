import sys

def solution():
    read = sys.stdin.readline
    testCase = int(read())
    ptrn = ('E', 'S', 'T', 'J')
    for t in range(testCase):
        minDist = float("inf")
        mbtiTypes = [0 for _ in range(16)]
        n = int(read())
        mbtiList = list(read().split())
        for mbti in mbtiList:
            idx = 0
            for i in range(4):
                if mbti[i] == ptrn[i]: idx += (0x1 << (3 - i))
            mbtiTypes[idx] += 1

        for i in range(16):
            if not mbtiTypes[i]: continue
            mbtiTypes[i] -= 1
            for j in range(i, 16):
                if not mbtiTypes[j]: continue
                mbtiTypes[j] -= 1
                for k in range(j, 16):
                    if not mbtiTypes[k]: continue
                    diff = 0
                    for l in range(4):
                        if ((k >> l) & 0x1) ^ ((j >> l) & 0x1): diff += 1
                        if ((k >> l) & 0x1) ^ ((i >> l) & 0x1): diff += 1
                        if ((j >> l) & 0x1) ^ ((i >> l) & 0x1): diff += 1
                    minDist = min(minDist, diff)
                mbtiTypes[j] += 1
            mbtiTypes[i] += 1
        print(minDist)

solution()