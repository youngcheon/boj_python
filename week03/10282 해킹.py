input = __import__('sys').stdin.readline
from heapq import heappop, heappush
inf = 10**9
def dj(start):
    distance = [inf]*(n+1)
    heap = []
    heappush(heap, (0,start))
    distance[start] = 0
    while heap:
        dist, now = heappop(heap)
        if distance[now] < dist:
            continue
        for t, c in graph[now]:
            cost = dist+c
            if distance[t] > cost:
                distance[t] = cost
                heappush(heap, (cost, t))
    return distance
for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a,s))
    computers = sum(list(map(lambda x : x < inf, dj(c))))
    time = max(list(map(lambda x : x if x < inf else 0, dj(c))))
    print(computers, time)

