input = __import__('sys').stdin.readline
inf = __import__('math').inf
from collections import defaultdict
from heapq import heappop, heappush
n, m = int(input()), int(input())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
start, end = map(int, input().split())
distance = [inf]*(n+1)
q = [(0, start,[start])]
while q:
    dist, now, path = heappop(q)
    if now == end:
        print(distance[end])
        print(len(path))
        print(*path)
        break
    for t, c in graph[now]:
        cost = dist+c
        if distance[t] <= cost:
            continue
        distance[t] = cost
        heappush(q, [cost, t, path+[t]])