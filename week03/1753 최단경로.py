input = __import__('sys').stdin.readline
from heapq import heappop, heappush
inf = 10**9
def dj(start):
    dp = [inf]*(v+1)
    heap = []
    heappush(heap, (0, start))
    dp[start] = 0
    while heap:
        dist, now = heappop(heap)
        if dp[now] < dist:
            continue
        for t, c in graph[now]:
            cost = dist+c
            if dp[t] > cost:
                dp[t] = cost
                heappush(heap, (cost,t))
    return dp
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
k = int(input())
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
answer = list(map(lambda x: 'INF' if x == inf else x, dj(k)[1:]))
print('\n'.join(map(str, answer)))