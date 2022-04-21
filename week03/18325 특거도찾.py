input = __import__('sys').stdin.readline
from collections import deque
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [0]*(n+1)
visited = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = 1
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    answer.append(i)
    print('\n'.join(map(str, sorted(answer))) if answer else -1)
bfs(x)