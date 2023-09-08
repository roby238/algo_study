n = int(input())

flowers = []
for _ in range(n):
    start_m, start_d, end_m, end_d = map(int, input().split())
    flowers.append((start_m * 100 + start_d, end_m * 100 + end_d))
flowers.sort()

end_date = 301 #현재 선택한 꽃의 종료일
last_end_date = 0 #선택한 꽃의 종료일 중 가장 큰 날짜
count = 0
i = 0

while flowers and end_date < 1201:
    ch = False #새로운 꽃 선택여부 체크
    while i < n and flowers[i][0] <= end_date :
        if flowers[i][1] > last_end_date:
            last_end_date = flowers[i][1]
            ch = True
        i += 1
    if not ch: #더이상 선택 or 확인할 수 있는 꽃이 없는 경우
        break
    count += 1
    end_date = last_end_date

print(count if end_date >= 1201 else 0)