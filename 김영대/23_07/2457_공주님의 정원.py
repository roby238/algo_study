import sys
def solution():
    dates = [0] * 13
    for i in range(2, 13):
        if i == 2 or i == 4 or i == 6 or i == 8 or i == 9 or i == 11:
            dates[i] = dates[i - 1] + 31
        elif i == 3:
            dates[i] = dates[i - 1] + 28
        elif i == 5 or i == 7 or i == 10 or i == 12:
            dates[i] = dates[i - 1] + 30

    read = sys.stdin.readline
    [n] = map(int, read().rstrip().split())

    flower = []
    for _ in range(0, n):
        month1, date1, month2, date2 = map(int, read().rstrip().split())
        s = dates[month1] + date1
        e = dates[month2] + date2 - 1
        if s <= dates[3]:
            s = dates[3] + 1
        if e > dates[11] + 30:
            e = dates[12] + 1
        flower.append([s, e])

    flower.sort()

    start = end = dates[3]
    count = 0
    for i in range(0, n):
        if start >= flower[i][0] and end <= flower[i][1]:
            end = flower[i][1]
        elif start < flower[i][0] \
            and flower[i][0] <= end + 1 \
            and end < flower[i][1]:
            start = end + 1
            end = flower[i][1]
            count += 1

        if end >= dates[11] + 30:
            break;

    if end >= dates[11] + 30:
        print(count)
    else:
        print(0)

solution()
