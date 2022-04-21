input = __import__('sys').stdin.readline
from collections import deque

m,n,h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append([i,j,k])
while q:
    z,x,y = q.popleft()
    for i in range(6):
        nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
        if 0<=nx<n and 0<=ny<m and 0<=nz<h and graph[nz][nx][ny] == 0:
            q.append((nz,nx,ny))
            graph[nz][nx][ny] = graph[z][x][y]+1
result = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
            result = max(result, graph[i][j][k])
print(result-1)