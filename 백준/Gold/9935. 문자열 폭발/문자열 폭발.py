import sys

string = input() #sys.stdin.readline.strip() 이거 왜 안되는거죠? ㅠㅠ
bomb = input() #sys.stdin.readline.strip()
bomblen = len(bomb)
stck = []

for i in range(len(string)):
  stck.append(string[i])
  #직전에 폭발을 했어도 -index slicing을 사용하면 나중에 새로 merge된 bomb도 한번에 처리가 가능하다. 즉 모든 edge case 처리 가능.
  if ''.join(stck[-bomblen:]) == bomb:
    for j in range(bomblen):
      stck.pop()

if stck:
  print("".join(stck))
else:
  print("FRULA")