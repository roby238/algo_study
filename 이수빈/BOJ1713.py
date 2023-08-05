F = []
N = int(input())
vote = int(input())
vote_n = list(map(int, input().split()))

for i in range(vote):
    nowvote_n = vote_n[i]
    check = False

    for j in range(len(F)):
        if F[j][0] == nowvote_n:
            F[j] = (nowvote_n, F[j][1] + 1, F[j][2])
            check = True
            break

    if not check:
        if len(F) < N:
            F.append((nowvote_n, 1, i))
        else:
            F.sort(key=lambda x: (x[1], x[2]))
            F[0] = (nowvote_n, 1, i)

F.sort(key=lambda x: x[0])
print(" ".join(str(candidate[0]) for candidate in F))