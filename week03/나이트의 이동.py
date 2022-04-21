input = __import__('sys').stdin.readline
from collections import deque
def bfs(sx, sy, ex, ey):
    q = deque()
    q.append((sx, sy))
    graph[sx][sy] = 1
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            break
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<l and 0<=ny<l and graph[nx][ny]==0:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[x][y]-1

dx = [2, -2, 2, -2, 1, 1, -1, -1]
dy = [1, 1, -1, -1, 2, -2, 2, -2]
t = int(input())
for _ in range(t):
    l  = int(input())
    graph = [[0]*l for _ in range(l)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    print(bfs(sx, sy, ex, ey))