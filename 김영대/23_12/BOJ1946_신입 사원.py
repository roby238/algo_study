import sys


def solution_prc():
    """
    Recruit volunteers without fails.
    :return:
    """
    read = sys.stdin.readline
    test_case = int(read())

    def cut_with_rank_proc(vol, pf, flag):
        """
        Sort by flag(0 or 1) and determine pass or fail by sorted points.
        :param vol: volunteer list
        :param pf: pass or fail info
        :param flag: 0 or 1
        :return:
        """
        volunteer.sort(key=lambda x: (x[1 + flag]))
        tmp_rank = float("inf")
        for i in range(n):
            if tmp_rank > vol[i][2 - flag]:
                tmp_rank = vol[i][2 - flag]
            else:
                pf[vol[i][0]] = 0

    def count_without_fail_proc(pf):
        """
        Count without fails.
        :param pf: pass or fail info
        :return: Count
        """
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
