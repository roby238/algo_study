import sys
origin = []
optionHead = []
optionOther = []
answer = []
isShortCut = [0] * 26
def solution():
    read = sys.stdin.readline
    n = int(read().rstrip())
    for _ in range(n):
        origin.append("")
        optionHead.append("")
        optionOther.append("")
        answer.append(-1)


    for i in range(n):
        origin[i] = list(read().rstrip())
        optionHead[i] += origin[i][0]
        optionOther[i] += " "
        for j in range(1, len(origin[i])):
            if origin[i][j - 1] == ' ':
                optionHead[i] += origin[i][j]
                optionOther[i] += " "
            else:
                optionHead[i] += " "
                optionOther[i] += origin[i][j]

    for i in range(n):
        for j in range(len(origin[i])):
            if optionHead[i][j] != ' ' and isShortCut[ord(optionHead[i][j].lower()) - 97] == 0:
                isShortCut[ord(optionHead[i][j].lower()) - 97] = 1
                answer[i] = j
                break;

        if answer[i] > -1:
            continue

        for j in range(len(origin[i])):
            if optionOther[i][j] != ' ' and isShortCut[ord(optionOther[i][j].lower()) - 97] == 0:
                isShortCut[ord(optionOther[i][j].lower()) - 97] = 1
                answer[i] = j
                break;

    for i in range(n):
        str = ""
        for j in range(len(origin[i])):
            if answer[i] == j:
                str += "[" + origin[i][j] + "]"
            else:
                str += origin[i][j]
        print(str)

solution()