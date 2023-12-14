import sys


def solution_prc():
    read = sys.stdin.readline
    test_case = int(read())

    def cut_with_rank_proc(vol, pf, flag):
        volunteer.sort(key=lambda x: (x[1 + flag]))
        tmp_rank = float("inf")
        for i in range(n):
            if tmp_rank > vol[i][2 - flag]:
                tmp_rank = vol[i][2 - flag]
            else:
                pf[vol[i][0]] = 0

    def count_without_fail_proc(pf):
        cnt = 0
        for i in range(n):
            if pf[i]:
                cnt += 1
        return cnt

    for _ in range(test_case):
        n = int(read())
        volunteer = []
        pass_or_fail = [1 for _ in range(n)]
        for i in range(n):
            volunteer.append([i] + list(map(int, read().split())))
        cut_with_rank_proc(volunteer, pass_or_fail, 0)
        cut_with_rank_proc(volunteer, pass_or_fail, 1)
        print(count_without_fail_proc(pass_or_fail))


solution_prc()
