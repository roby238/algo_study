key, menu = [] , []
N = int(input()) 
end = 0

def keyword(x):
  key.append(x)
  if x.isupper(): key.append(x.lower())
  else: key.append(x.upper())
  x = '['+str(x)+']'
  return x
  
for _ in range(N):
  op = list(input().strip())
  for i in range(len(op)):
    if op[0] in key  and op[i-1] == ' ' and op[i] not in key:
      op[i] = keyword(op[i])
      menu.append(''.join(op))
      end = N
      break
  
  if end == N:
    end = 0
    continue

  for i in range(len(op)):
    if op[i] not in key and op[i] != ' ':
      op[i] = keyword(op[i])
      break
  menu.append(''.join(op))
  
print('\n'.join(menu))
