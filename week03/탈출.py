input = __import__('sys').stdin.readline
inf = __import__('math').inf
from collections import deque

def bfs():
    while q:
        x, y = q.popleft()
        if graph[xx][yy] == 'S':
            # S 가 D에 도착하면
            return distance[xx][yy]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<r and 0<=ny<c:
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S'
                    distance[nx][ny] = distance[x][y]+1
                    q.append((nx,ny))
                elif (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    q.append((nx,ny))
    return 'KAKTUS'

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
distance = [[0]*c for _ in range(r)]
q = deque()
# 고슴도치 S, 동굴 D
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            q.append((i,j))
        elif graph[i][j] == 'D':
            xx, yy = (i,j)
            
# 물 *
for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            q.append((i,j))

print(bfs())