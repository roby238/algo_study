import copy
import sys


def solution_proc():
    read = sys.stdin.readline
    n, m, k = map(int, read().split())
    array = [list(map(int, read().split())) for _ in range(n)]
    rotate_info = [list(map(int, read().split())) for _ in range(k)]
    visit = [0 for _ in range(k)]
    permutations = []
    permutation = []
    dy, dx = (0, 0, 1, 0, -1), (0, 1, 0, -1, 0)

    def get_permutation(depth):
        if depth == k:
            tmp = permutation.copy()
            permutations.append(tmp)
            return

        for i in range(0, k):
            if visit[i]: continue
            permutation.append(i)
            visit[i] = 1
            get_permutation(depth + 1)
            permutation.pop()
            visit[i] = 0

        return permutations

    def get_direction(y, x):
        if y < -x and y <= x: return 1
        if -x <= y < x: return 2
        if y > -x and y >= x: return 3
        if x < y <= -x: return 4
        return 0

    def rotate(idx, curr_array):
        next_array = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                next_array[i][j] = curr_array[i][j]
        r, c, s = rotate_info[idx]
        r -= 1
        c -= 1
        for i in range(r - s, r + s + 1):
            for j in range(c - s, c + s + 1):
                k = get_direction(i - r, j - c)
                next_array[i + dy[k]][j + dx[k]] = curr_array[i][j]

        return next_array

    permutations = get_permutation(0)
    min_sum = float("inf")
    for permutation in permutations:
        new_array = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                new_array[i][j] = array[i][j]
        for idx in permutation:
            new_array = rotate(idx, new_array)
        for row in new_array:
            min_sum = min(min_sum, sum(row))
    print(min_sum)


solution_proc()
