n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

l = 0
r = n-1

gap = abs(liquid[l] + liquid[r])
result = [liquid[l], liquid[r]]


while l < r:
    le = liquid[l]
    ri = liquid[r]

    cal = le + ri
  
    if abs(cal) < gap:
        gap = abs(cal)
        result = [le, ri]
        if gap == 0:
          break
    if cal < 0:
        l += 1
    else:
        r -= 1

print(result[0], result[1])
