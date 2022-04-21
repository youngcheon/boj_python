input = __import__('sys').stdin.readline 
from collections import deque
def dfs(n):
    print(n, end=' ')
    visited[n] = 1
    for i in graph[n]:
        if not visited[i]:
            dfs(i)
def bfs(n):
    visited[n] = 1
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
graph = list(map(lambda x: sorted(x), graph))
dfs(v)
visited = [0]*(n+1)
print()
bfs(v)