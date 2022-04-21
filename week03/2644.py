input = __import__('sys').stdin.readline
from collections import deque, defaultdict
def bfs(s):
    q = deque()
    q.append(s)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i) 
    return visited[end] if visited[end] else -1
n = int(input())
visited = [0]*(n+1)
graph = defaultdict(list)
start, end = map(int, input().split())
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(bfs(start))