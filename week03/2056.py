input = __import__('sys').stdin.readline
from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
indgree = [0]*(n+1)
for j in range(1, n+1):
    li = list(map(int, input().split()))
    li.insert(2, j)
    print(li[2:])
    cost = li[0]
    for i in range(li[1]):
        graph[li[2:][i-1]].append((li[2:][i], cost))
        indgree[li[2:][i]] += 1
print(graph)
q = deque()
for i in range(n):
    if not indgree[i]:
        q.append(i)
result = 0
while q:
    now = q.popleft()
    for i, cost in graph[now]:
        indgree[i] -= 1
        if not indgree[i]:
            result+=cost
            q.append(i)
print(result)