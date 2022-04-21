import sys
from collections import deque
input = sys.stdin.readline
dx= [1,-1,-2,-2,-1,1,2,2]
dy = [2,2,1,-1,-2,-2,-1,1]
def bfs(sx, sy, ax, ay):
    q = deque()
    q.append((sx,sy))
    graph[sx][sy] = 1
    while q:
        a, b = q.popleft()
        if (a,b) == (ax,ay):
            print(graph[ax][ay]-1)
            return
        for i in range(8):
            nx = a+dx[i]
            ny = b+dy[i]
            if 0<=nx<l and 0<=ny<l and graph[nx][ny] == 0:
                q.append((nx,ny))
                graph[nx][ny] = graph[a][b] + 1
t = int(input())
for _ in range(t):
    l = int(input())
    graph = [[0]*l for _ in range(l)]
    x, y = map(int, input().split())
    x1, y1 = map(int, input().split())
    bfs(x, y, x1, y1)
        