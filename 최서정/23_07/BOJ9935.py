N  = list(input()) # 문자열 입력받기
bomb = input() # 폭발 문자열
stack  = [] # 스택 선언

for i in range(len(N)):
  stack.append(N[i]) # 문자열의 길이만큼 for문 돌리면서 한 글자씩 stack에 넣기
  if len(stack) >= len(bomb): # stack 의 길이가 폭발 문자열의 길이와 같거나 큰 경우
    if ''.join(stack[-len(bomb):]) == bomb: #끝에서부터 폭발문자열 길이만큼의 단어와 폭발문자열 비교
      for j in range(len(bomb)):
        stack.pop() # 같다면 삭제해줌

if len(stack): # stack에 남아있는 문자열이 있으면 string 형태로 바꾸어 출력
  print(''.join(stack))
else: # 아니면 FRULA 출력
  print('FRULA')
