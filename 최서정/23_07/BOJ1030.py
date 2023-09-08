import sys
inp = sys.stdin.readline

s,N,K,R1,R2,C1,C2 = map(int,inp().split())
length = N**s

def fractal(length,r,c):
  black = length/N
  if length == 1: return 0
  elif black * (N-K)//2 <= r < black * (N+K)//2 and black*(N-K)//2 <= c < black*(N+K)//2:
    return 1
  r %= black
  c %= black
  return fractal(length//N,r,c)
     
for i in range(R1,R2+1):
  for j in range(C1,C2+1):
    print(fractal(length,i,j), end='')
  print()
