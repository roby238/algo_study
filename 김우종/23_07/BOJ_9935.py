# BOJ_9935
# 문자열 폭발

import sys

# input string
in_string = ""
# input bomb
in_bomb = ""
stack = list()


# input function
def get():
    # input string
    global in_string
    in_string = sys.stdin.readline().rstrip()

    # 예외 처리 - 수정 필요
    if len(in_string) < 1 or len(in_string) > 1000000:
        print("error")
        sys.exit(1)

    # input bomb
    global in_bomb
    in_bomb = sys.stdin.readline().rstrip()

    # 예외 처리 - 수정 필요
    if len(in_bomb) < 1 or len(in_bomb) > 36:
        print("")
        sys.exit(1)


def bomb_action(target, bomb):
    global stack

    for i in range(len(target)):
        stack.append(target[i])
        if ''.join(stack[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()

    if len(stack) == 0:
        print("FRULA")
    else:
        print(''.join(stack))


# run
get()
bomb_action(in_string, in_bomb)
