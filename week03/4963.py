from sys import setrecursionlimit, stdin,stdout
setrecursionlimit(10**6)
input = stdin.readline
print = stdout.write

def dfs(x,y):
    if x<=-1 or x>=w or y<= -1 or y>=h:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x-1,y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x+1,y+1)
        dfs(x-1,y-1)
        dfs(x+1,y-1)
        dfs(x-1,y+1)
        return True
    return False
while 1:
    w, h = 0, 0
    arr = []
    count = 0
    w, h = map(int,input().split())
    if w==0 and h==0 : break
    graph = [list(map(int, input().split())) for _ in range(h)]
    for i in range(w):
        for j in range(h):
            if dfs(i, j) == True:
                count += 1
    print('{}\n'.format(count))