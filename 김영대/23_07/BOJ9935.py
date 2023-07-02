# BOJ9935: 문자열 폭발
# 문자열 터뜨리는 함수
def strExp():
    str = input()
    bomb = input()
    # stack
    stack = []
    for i in str:
        stack.append(i)
        # stack의 마지막부터 조사한 문자열을 bomb와 비교
        if("".join(stack[-len(bomb):]) == bomb):
            # bomb 길이만큼 pop
            for j in bomb:
                # 이 부분을 replace나 stack[-len(bomb):]로 처리하려 하면 시간초과;;;
                stack.pop(len(stack) - 1)
    # 빈 리스트인지 검증
    if(len(stack) == 0): print("FRULA")
    else : print("".join(stack))

if __name__ == '__main__':
    strExp()