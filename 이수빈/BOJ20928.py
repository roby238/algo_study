N, M = map(int, input().split())
p = list(map(int, input().split()))
x = list(map(int, input().split()))

max_point = min(M, p[0] + x[0])
count = [-1] * (M + 1)

for i in range(p[0], max_point + 1):
    count[i] = 0

for i in range(1, N):
    next_point = min(p[i] + x[i], M)
    if p[i] <= max_point and next_point > max_point:
        count[max_point + 1:next_point + 1] = [count[p[i]] + 1] * (next_point - max_point)
        max_point = next_point

print(count[M])