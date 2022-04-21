input = __import__('sys').stdin.readline
from math import inf

n, m = int(input()), int(input())
cost = [[inf] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)

# 플로이드
for k in range(n):
    cost[k][k] = 0
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

for i in cost:
    print(' '.join(map(lambda x: '0' if x==inf else str(x), i)))