S = input()

#현재 위치에서 다음 위치로 이동하는 거리
def dist(a, b, c, d):
    return 0 if c == -1 or d == -1 else abs(a - c) + abs(c - d) + abs(d - b)

def solve(S):
    s = len(S)
    cnt = [[-1] * s for _ in range(26)]
    alpha_first = [50] * 26
    alpha_last = [-1] * 26
    ch = [False] * 26

    for i, char in enumerate(S):
        index = ord(char) - ord('a')
        ch[index] = True
        alpha_first[index] = min(alpha_first[index], i)
        alpha_last[index] = max(alpha_last[index], i)

    def dp(alpha, j):
        if alpha == 26:
            return 0
        if cnt[alpha][j] != -1:
            return cnt[alpha][j]

        count = float('inf')
        j_first, j_last = alpha_first[alpha], alpha_last[alpha]

        if ch[alpha]:
            for i in range(s):
                count = min(count, dp(alpha + 1, i) + min(dist(j, i, j_first, j_last), dist(j, i, j_last, j_first)))
        else:
            count = dp(alpha + 1, j)

        cnt[alpha][j] = count
        return count

    return dp(0, 0) + s #문자열 길이만큼 엔터 클릭하는 횟수 추가

print(solve(S))