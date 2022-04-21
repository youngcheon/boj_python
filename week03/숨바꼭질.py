input = __import__('sys').stdin.readline
from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            break
        for i in (x+1,x-1,2*x):
            if 0<=i<=100000 and not graph[i]:
                graph[i] = graph[x]+1
                q.append(i)
    return graph[x]
n, k = map(int, input().split())
graph = [0]*100001
print(bfs(n))