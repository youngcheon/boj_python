input = __import__('sys').stdin.readline
from heapq import heappop, heappush
inf = 10**9
def dj(s):
    dp = [inf]*(n+1)
    heap = []
    heappush(heap, (0, s))
    dp[s] = 0
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
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
result = 0
for i in range(1, n+1):
    result = max(dj(i)[x]+dj(x)[i], result)
print(result)