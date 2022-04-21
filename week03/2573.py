input = __import__('sys').stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()
day = 0

def bfs(a,b):
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                elif graph[nx][ny] == 0:
                    count[x][y] += 1
    return 1

# 빙산이 분리될때까지 돌아줌
while True:
    visited = [[False]*m for _ in range(n)]
    count = [[0]*m for _ in range(n)]
    result = [bfs(i,j) for i in range(n) for j in range(m) if graph[i][j]>0 and not visited[i][j]]
    # 빙산을 깎아줌      
    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j] if graph[i][j]>=count[i][j] else graph[i][j] 
    ice = len(result) 
    if ice == 0: 
        print(0)
        break
    elif ice >= 2: 
        print(day)
        break
    day += 1