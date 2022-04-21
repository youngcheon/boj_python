input = __import__('sys').stdin.readline
from collections import deque
def bfs(x,y):
    count = 1
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        graph[x][y] = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]:
                q.append((nx,ny))
                graph[nx][ny] = 0
                count += 1
    return count
n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dx, dy = [1,-1,0,0], [0,0,-1,1]
result = []
answer = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            answer += 1
            result.append(bfs(i,j))
print(str(answer)+'\n'+'\n'.join(map(str, sorted(result))))