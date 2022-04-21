input = __import__('sys').stdin.readline
inf = __import__('math').inf
from heapq import heappop, heappush

def dj():
    heap = []
    heappush(heap, (0, (0,0)))
    crush[0][0] = 0
    dx, dy = [1,-1,0,0], [0,0,-1,1]
    while heap:
        count, (x, y) = heappop(heap)
        if x == n-1 and y == m-1:
            # 출구일경우 종료
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and crush[nx][ny]<0:
                crush[nx][ny] = count
                if maze[nx][ny] == '1':
                    heappush(heap, (count+1, (nx, ny)))
                else:
                    heappush(heap, (count, (nx, ny)))

m, n = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(n)]
crush = [[-1]*m for _ in range(n)]
dj()
print(crush[n-1][m-1])