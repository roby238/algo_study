import sys
input = sys.stdin.readline

# 1. 입력 받기
str = list(input().rstrip())
bomb = list(input().rstrip())
tmp = []

# 2. 문자열 폭발시키기
for i in range(len(str)):
    tmp.append(str[i])
    if bomb[-1] == tmp[-1]:
        if len(bomb) > len(tmp):
            continue
        check = True
        for j in range(len(bomb)):
            if tmp[len(tmp) - len(bomb) + j] != bomb[j]:
                check = False
                break
        if check:
            for _ in range(len(bomb)):
                tmp.pop()

if len(tmp) > 0:
    print("".join(tmp))
else: print("FRULA")
