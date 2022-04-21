input = __import__('sys').stdin.readline
from collections import deque

n, k = map(int, input().split())
virus = []
graph = []
dx, dy = [-1,1,0,0], [0,0,-1,1]
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j, 0))
s, xx, yy = map(int, input().split())
virus.sort()
q = deque(virus)
while q:
    v, x, y, time = q.popleft()
    if time == s:
        break
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0:
            graph[nx][ny] = v
            q.append((v, nx, ny, time+1))
print(graph[xx-1][yy-1])