input = __import__('sys').stdin.readline
from collections import deque

def bfs():
    dx = [-1,1,0,0]; dy = [0,0,-1,1]
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    while q:
        x, y, crash = q.popleft()
        if x == n-1 and y ==m-1:
            return visited[x][y][crash]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0 and visited[nx][ny][crash] ==0:
                    q.append((nx,ny,crash))
                    visited[nx][ny][crash] = visited[x][y][crash]+1
                if graph[nx][ny] == 1 and crash ==0:
                    q.append((nx,ny,crash+1))
                    visited[nx][ny][crash+1] = visited[x][y][crash]+1
    return -1
n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
print(bfs())