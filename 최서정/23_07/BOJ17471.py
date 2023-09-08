import sys, itertools, collections

def bfs(x):
    s = x[0]
    q = collections.deque([s])
    visited = set([s])
    sum = 0
    while q:
        v = q.popleft()
        sum += p[v]
        for i in divide[v]:
            if i not in visited and i in x:
                q.append(i)
                visited.add(i)
    return sum, len(visited)

n = int(sys.stdin.readline().strip())
p = [int(x) for x in sys.stdin.readline().split()]
divide = collections.defaultdict(list)
result = 1e9

for i in range(n):
    inp = [int(x) for x in sys.stdin.readline().split()]
    for j in range(1, inp[0]+1):
        divide[i].append(inp[j]-1)

for i in range(1, n//2 + 1):
    case = list(itertools.combinations(range(n), i))
    for c in case:
        sum1, visit1 = bfs(c)
        sum2, visit2 = bfs([i for i in range(n) if i not in c])
        if visit1 + visit2 == n:
            result = min(result, abs(sum1 - sum2))

if result != 1e9:
    print(result)
else:
    print(-1)
