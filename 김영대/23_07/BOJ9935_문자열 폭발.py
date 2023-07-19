def strExp():
    str = input()
    bomb = input()
    ans = []

    for i in str:
        ans.append(i)
        if("".join(ans[-len(bomb):]) == bomb):
            for j in bomb:
                ans.pop(len(ans) - 1)

    if(len(ans) == 0):
        print("FRULA")
    else:
        print("".join(ans))

if __name__ == '__main__':
    strExp()