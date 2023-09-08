n, m = map(int,input().split())
runtime = list(map(int,input().split()))

start, end = max(runtime) , sum(runtime)

while start <= end:
    s,cnt = 0,1
    mid = (start + end) // 2 

    for time in runtime:
        if s + time > mid:
            cnt += 1
            s = 0
        s += time 

    if cnt <= m:
        result = mid
        end = mid - 1
    else: start = mid + 1
    
print(result)
