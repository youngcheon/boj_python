input = __import__('sys').stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs(n):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
count = 0
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        count += 1
print(count)