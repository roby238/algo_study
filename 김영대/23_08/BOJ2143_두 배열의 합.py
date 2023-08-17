import sys


def solution():
    read = sys.stdin.readline
    t = int(read())
    n = int(read()); a = list(map(int, read().split()))
    m = int(read()); b = list(map(int, read().split()))

    sum_a = [0 for _ in range(n)]; sum_a[0] = a[0]
    sum_b = [0 for _ in range(m)]; sum_b[0] = b[0]
    sa = 0
    for i in range(n):
        sa += a[i]
        sum_a[i] = sa
    sb = 0
    for i in range(m):
        sb += b[i]
        sum_b[i] = sb
    va = sum_a; vb = sum_b
    for i in range(n):
        for j in range(i + 1, n):
            va.append(sum_a[j] - sum_a[i])
    for i in range(m):
        for j in range(i + 1, m):
            vb.append(sum_b[j] - sum_b[i])

    va.sort(); vb.sort()

    pa = 0; pb = len(vb) - 1; cnt = 0
    while (pa < len(va) and 0 <= pb):
        tmp = va[pa] + vb[pb]
        if t < tmp: pb -= 1
        elif tmp < t: pa += 1
        else:
            ca = 1;
            cb = 1
            while (pa < len(va) - 1 and va[pa + 1] == va[pa]): pa += 1; ca += 1
            while (0 < pb and vb[pb - 1] == vb[pb]): pb -= 1; cb += 1
            cnt += ca * cb
            pa += 1; pb -= 1
    print(cnt)


solution()