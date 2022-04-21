input = __import__('sys').stdin.readline
from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
d = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    d[b] += 1
    
result = []

q = deque([i for i in range(1,n+1) if not d[i]])
while q:
    now = q.popleft()
    result.append(now)
    for i in g[now]:
        d[i] -= 1
        if not d[i]:
            q.append(i)
print(*result)