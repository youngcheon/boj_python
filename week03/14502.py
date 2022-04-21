input = __import__('sys').stdin.readline
from collections import deque
import copy
n,m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx, dy = [1,-1,0,0], [0,0,-1,1]
def bfs():
    global answer
    q = deque()
    #바이러스
    temp = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append((i,j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx,ny))
    count = 0
    for i in range(n):
        count += temp[i].count(0)
    answer = max(answer, count)

def makewall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makewall(count+1)
                graph[i][j] = 0

answer = 0
makewall(0)
print(answer)