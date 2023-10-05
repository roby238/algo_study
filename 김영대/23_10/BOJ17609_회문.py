import sys
def solution():
    read = sys.stdin.readline
    n = int(read())
    for i in range(n):
        str = read().rstrip()
        left, right = 0, len(str) - 1
        cntWithLeftCheck, flagLeft = 0, False
        while left < right:
            if str[left] == str[right]:
                cntWithLeftCheck += 1
                left += 1
                right -= 1
            else:
                if (not flagLeft) and str[left] == str[right - 1]:
                    right -= 1
                    flagLeft = True
                else: break

        left, right = 0, len(str) - 1
        cntWithRightCheck, flagRight = 0, False
        while left < right:
            if str[left] == str[right]:
                cntWithRightCheck += 1
                left += 1
                right -= 1
            else:
                if (not flagRight) and str[left + 1] == str[right]:
                    left += 1
                    flagRight = True
                else: break

        if (not flagLeft and not flagRight) and \
                max(cntWithLeftCheck, cntWithRightCheck) == (len(str) // 2):
            print(0)
        elif (flagLeft or flagRight) and \
            max(cntWithLeftCheck, cntWithRightCheck) == ((len(str) - 1) // 2):
            print(1)
        else: print(2)

solution()