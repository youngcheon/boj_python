from heapq import heappush, heappop
def bfs(height, x, y) :
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = []
    heappush(q, (-height, x, y))
    visit[x][y] = 1
    while q :
        height, x, y = heappop(q)
        if x == row - 1 and y == col - 1 :
            continue
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and graph[nx][ny] < -height :
                if not visit[nx][ny] :
                    heappush(q, (-graph[nx][ny], nx, ny))
                visit[nx][ny] += visit[x][y]
    return
row, col = map(int, input().split())
graph = [[int(x) for x in input().split()] for _ in range(row)]
visit = [[0] * col for _ in range(row)]
bfs(graph[0][0], 0, 0) #height, start x, start y
print(visit[-1][-1])
for i in visit:
    print(i)