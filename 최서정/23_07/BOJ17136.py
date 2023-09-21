board = [list(map(int, input().split())) for _ in range(10)]
paper = [0, 5, 5, 5, 5, 5]
result = set()

def length_(y, x):
    length = 1
    for l in range(2, min(10 - y, 10 - x, 5) + 1):
        for i in range(y, y + l):
            for j in range(x, x + l):
                if board[i][j] == 0:
                    return length
        length += 1
    return length

def fold(y, x, length):
    for i in range(y, y + length):
        for j in range(x, x + length):
            board[i][j] = 0

def unfold(y, x, length):
    for i in range(y, y + length):
        for j in range(x, x + length):
            board[i][j] = 1

def dfs(cnt):
    for i in range(0, 10):
        for j in range(0, 10):
            if board[i][j] == 1:
                length = length_(i, j)
                for l in range(length, 0, -1):
                    if paper[l]:
                        fold(i, j, l)
                        paper[l] -= 1
                        result.add(dfs(cnt + 1))
                        unfold(i, j, l)
                        paper[l] += 1
                if result:
                    return min(result)
                else:
                    return -1
    return cnt

result.add(dfs(0))

if -1 in result:
    result.remove(-1)
print(min(result) if result else -1)
