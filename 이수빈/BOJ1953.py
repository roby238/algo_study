n = int(input())
hate = [[] for _ in range(n+1)]
check = [0] * (n+1)
team_blue, team_white = [], []

def dfs(node, team):
    check[node] = team
    for i in hate[node]:
        if check[i] == 0:
            dfs(i, 'blue' if team == 'white' else 'white')

for j in range(1, n+1):
    hate_l = list(map(int, input().split()))
    hate[j] = hate_l[1:]

for j in range(1, n+1):
    if check[j] == 0:
        dfs(j, 'blue')

for j in range(1, n+1):
    if check[j] == 'blue':
        team_blue.append(j)
    else:
        team_white.append(j)

print(len(team_blue), *team_blue)
print(len(team_white), *team_white)