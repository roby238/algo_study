from collections import defaultdict

T = int(input())
n = int(input())
arr_A = list(map(int, input().split()))
m = int(input())
arr_B = list(map(int, input().split()))

checking = defaultdict(int)

result = 0
for i in range(n):
    for j in range(i, n, 1):
        checking[sum(arr_A[i:j+1])] += 1
for i in range(m):
    for j in range(i, m, 1):
      result += checking[T - sum(arr_B[i:j+1])]

print(result)
