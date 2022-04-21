input = __import__('sys').stdin.readline
from collections import deque, defaultdict

n,m = map(int, input().split())
graph = defaultdict(list)
indegree = [0]*(n+1)
isu = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

q=deque()
for i in range(1,n+1):
    if not indegree[i]:
        q.append((i,1)) #1학기 이수가능
        isu[i] = 1

while q:
    now, count = q.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append((i,count+1))
            isu[i] = count+1
print(*isu[1:])