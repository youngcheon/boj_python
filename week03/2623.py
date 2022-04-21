input = __import__('sys').stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
d = [0]*(n+1)
for i in range(m):
    singers = list(map(int, input().split()))
    for s in range(1, singers[0]):
        graph[singers[s]].append(singers[s+1])
        d[singers[s+1]] += 1

q = deque()
result = []
for i in range(1, n+1):
    if d[i] == 0:
        q.append(i)
        
while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        d[i] -= 1
        if not d[i]:
            q.append(i)

print(0 if len(result) != n else '\n'.join(map(str, result)))