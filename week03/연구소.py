input = __import__('sys').stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
graph_min = min(map(min, graph))
graph_max = max(map(max, graph))
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,safe):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]; ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] >= safe and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))

max_safe_area = graph_min
for safe in range(graph_min, graph_max+1):
    visited = [[0]*n for _ in range(n)]
    temp = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= safe and visited[i][j] == 0:
                bfs(i, j, safe)
                temp += 1
    if temp > max_safe_area:
        max_safe_area = temp
print(max_safe_area)