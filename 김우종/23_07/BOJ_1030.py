# BOJ_1030
# 프렉탈 평면


def solution():
    s, n, k, r1, r2, c1, c2 = map(int, input().split())
    meaningful_square = dict()
    meaningful_square[s] = [[r1, r2], [c1, c2]]
    fractal_old = [[0]]
    fractal_new = list()

    if s == 0:
        print(0)
    else:
        for i in range(s):
            meaningful_square[s - i - 1] = [[meaningful_square.get(s - i)[0][0] // n, meaningful_square.get(s - i)[0][1] // n],
                                            [meaningful_square.get(s - i)[1][0] // n, meaningful_square.get(s - i)[1][1] // n]]

        for i in range(s):
            meaningful_square.get(s - i)[0][0] = meaningful_square.get(s - i)[0][0] - meaningful_square.get(s - i - 1)[0][0] * n
            meaningful_square.get(s - i)[0][1] = meaningful_square.get(s - i)[0][1] - meaningful_square.get(s - i - 1)[0][0] * n
            meaningful_square.get(s - i)[1][0] = meaningful_square.get(s - i)[1][0] - meaningful_square.get(s - i - 1)[1][0] * n
            meaningful_square.get(s - i)[1][1] = meaningful_square.get(s - i)[1][1] - meaningful_square.get(s - i - 1)[1][0] * n

        for i in range(s):
            fractal_new = [[0 for _ in range((meaningful_square.get(i)[1][1] - meaningful_square.get(i)[1][0] + 1) * n)]
                           for _ in range((meaningful_square.get(i)[0][1] - meaningful_square.get(i)[0][0] + 1) * n)]
            for j in range(meaningful_square.get(i)[0][0], meaningful_square.get(i)[0][1] + 1):
                for l in range(meaningful_square.get(i)[1][0], meaningful_square.get(i)[1][1] + 1):
                    if fractal_old[j][l] == 1:
                        for y in range((j - meaningful_square.get(i)[0][0]) * n,
                                       (j - meaningful_square.get(i)[0][0] + 1) * n):
                            for x in range((l - meaningful_square.get(i)[1][0]) * n,
                                           (l - meaningful_square.get(i)[1][0] + 1) * n):
                                fractal_new[y][x] = 1
                    else:
                        for y in range((j - meaningful_square.get(i)[0][0]) * n + int((n - k) / 2),
                                       (j - meaningful_square.get(i)[0][0]) * n + int((n - k) / 2) + k):
                            for x in range((l - meaningful_square.get(i)[1][0]) * n + int((n - k) / 2),
                                           (l - meaningful_square.get(i)[1][0]) * n + int((n - k) / 2) + k):
                                fractal_new[y][x] = 1
            fractal_old = fractal_new

        for i in range(meaningful_square.get(s)[0][0], meaningful_square.get(s)[0][1] + 1):
            for j in range(meaningful_square.get(s)[1][0], meaningful_square.get(s)[1][1] + 1):
                print(fractal_new[i][j], end='')
            print()


if __name__ == "__main__":
    solution()
