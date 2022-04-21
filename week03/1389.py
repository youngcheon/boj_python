from collections import deque, defaultdict
input = __import__('sys').stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(num):
    bacon = [0]*(n+1)
    q = deque()
    visited[num] = 1
    q.append(num)
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                bacon[i] = bacon[now] + 1
                q.append(i)
                visited[i] =1 
    return sum(bacon)

result =  []
for i in range(1,n+1):
    visited = [0]*(n+1)
    result.append(bfs(i))

print(result.index(min(result))+1)