import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
graph = defaultdict(list)
visited = [0]*(n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(s):
    for i in graph[s]:
        if not visited[i]:
            visited[i] = s
            dfs(i)
dfs(1)
print('\n'.join(map(str, visited[2:])))