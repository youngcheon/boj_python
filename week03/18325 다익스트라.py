input = __import__('sys').stdin.readline
from heapq import heappop, heappush
inf = 10**9

def dj(start):
    dp = [inf]*(n+1)
    heap = []
    heappush(heap, (0,start))
    dp[start] = 0
    while heap:
        dist, now = heappop(heap)
        if dp[now] < dist:
            continue
        for t,c in graph[now]:
            cost = dist+c
            if dp[t] > cost:
                dp[t] = cost
                heappush(heap, (cost, t))
                
    return dp

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append((b,1))
answer = [index for index, item in enumerate(dj(x)) if item == k]
if answer:
    print('\n'.join(map(str, answer)))
else:
    print(-1)