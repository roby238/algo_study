import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) 

n,m,x = map(int,input().split())
town = [[] for i in range(n+1)]

dis = [INF] *(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    town[a].append((b,c))

def dijkstra(s):
    q=[]
    heapq.heappush(q,(0,s))
    dis[s]=0 
    while q:
        dist,now = heapq.heappop(q) 
        
        for i in town[now]:
            cost = dist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
value=[0]*(1+n)

for i in range(1,n+1):
    if i == x:
        continue
    dis = [INF] * (n + 1)
    dijkstra(i)
    value[i] = dis[x] 
    dis = [INF] * (n + 1)
    dijkstra(x)
    value[i] += dis[i]

print(max(value))
