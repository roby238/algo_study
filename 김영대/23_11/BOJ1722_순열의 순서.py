import sys
def solution_proc():
    read = sys.stdin.readline
    n = int(read())
    factorial = [1 for _ in range(n)]
    line = list(map(int, read().split()))

    def n_factorial(m):
        for i in range(1, m):
            factorial[i] = i * factorial[i - 1]

    n_factorial(n)

    def get_kth_permutation(k):
        visit_info = [0 for _ in range(n + 1)]
        permutation = ""
        for i in range(n):
            target = (k // factorial[n - 1 - i]) + 1
            idx = 1
            for j in range(1, n + 1):
                if visit_info[j]: continue
                if target == idx:
                    permutation += str(j) + " "
                    visit_info[j] = 1
                    break
                idx += 1
            k %= factorial[n - 1 - i]
        return permutation

    def get_k_proc(p):
        visit_info = [0 for _ in range(n + 1)]
        idx = 1
        for i in range(n - 1):
            cnt = 0
            for j in range(1, p[i] + 1):
                if not visit_info[j]: cnt += 1
            idx += (cnt - 1) * factorial[n - 1 - i]
            visit_info[p[i]] = 1
        return idx

    if line[0] == 1:
        print(get_kth_permutation(line[1] - 1))
    else:
        print(get_k_proc(line[1:]))

solution_proc()