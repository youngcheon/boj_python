input = __import__('sys').stdin.readline
from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0]*(n+1)


q = deque()
q.append(1)
def bfs():
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = now
                q.append(i)
bfs()
print('\n'.join(map(str, visited[2:])))