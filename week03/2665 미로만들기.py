input = __import__('sys').stdin.readline
inf = __import__('math').inf
from heapq import heappop, heappush

def dj():
    heap = [(0, (0,0))]
    wall[0][0] = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while heap:
        count, (x, y) = heappop(heap)
        if x == n-1 and y == n-1:
            break
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and wall[nx][ny]==inf:
                wall[nx][ny] = count
                heappush(heap, (count+(maze[nx][ny] == '0'),(nx, ny)))
n = int(input())
maze = [list(input().rstrip()) for _ in range(n)]
wall = [[inf]*n for _ in range(n)]
dj()
print(wall[n-1][n-1])