alpha = []
low = []
high = []
pressCount = 100000007
def dfs(idx, presentCount, pos):
    if idx == 26:
        global pressCount
        pressCount = min(pressCount, presentCount)
        return
    if alpha[idx] != 0:
        if (low[idx] <= pos and pos <= high[idx]):
            presentCount += 2 * (pos - low[idx]) + high[idx] - pos
            dfs(idx + 1, presentCount, high[idx])
            presentCount -= 2 * (pos - low[idx]) + high[idx] - pos

            presentCount += pos - low[idx] + 2 * (high[idx] - pos)
            dfs(idx + 1, presentCount, low[idx])
            presentCount -= pos - low[idx] + 2 * (high[idx] - pos)
        elif (pos <= low[idx]):
            presentCount += high[idx] - pos
            dfs(idx + 1, presentCount, high[idx])
            presentCount -= high[idx] - pos
        elif (pos >= high[idx]):
            presentCount += pos - low[idx]
            dfs(idx + 1, presentCount, low[idx])
            presentCount -= pos - low[idx]
    else:
        dfs(idx + 1, presentCount, pos)
def solution():
    str = list(input())
    for i in range(26):
        low.append(50)
        high.append(-1)
        alpha.append(0)
    for i in range(len(str)):
        low[ord(str[i]) - 97] = min(low[ord(str[i]) - 97], i)
        high[ord(str[i]) - 97] = max(high[ord(str[i]) - 97], i)
        alpha[ord(str[i]) - 97] += 1
    dfs(0, len(str), 0)
    print(pressCount)

if __name__ == '__main__':
    solution()
