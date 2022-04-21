input = __import__('sys').stdin.readline
from heapq import heappush,heappop
inf = 10**9
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1, v2 = map(int, input().split())
def dj(start,end):
    distance = [inf]*(n+1)
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for t,c in graph[now]:
            cost = dist + c
            if distance[t] > cost:
                distance[t] = cost
                heappush(q, (cost, t))
    return distance[end]
answer = min(dj(1,v1)+dj(v1,v2)+dj(v2,n), dj(1,v2)+dj(v2,v1)+dj(v1,n))
print(answer if answer<inf else -1)
