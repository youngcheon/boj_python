sys = __import__('sys').stdin.readline
from collections import deque
n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
graph2 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        graph2[i][j] = graph[i][j].replace('G','R')
visited = [[0]*n for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(graph, x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        color = graph[x][y]
        for i in range(4):
            nx,ny= x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==color:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
count = 0
count2= 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(graph, i,j)
            count += 1
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(graph2, i,j)
            count2 += 1
print(count,count2)