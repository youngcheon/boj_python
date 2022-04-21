input = __import__('sys').stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or (graph[i][k]+graph[k][j] == 2):
                graph[i][j] = 1

for i in graph:
    print(*i) 