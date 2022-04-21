input = __import__('sys').stdin.readline
from math import inf

n, m = map(int, input().split())
cost = [[inf]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    cost[a-1][b-1] = 1
    cost[b-1][a-1] = 1

for k in range(n):
    cost[k][k] = 0
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])
ans = []
for i in cost:
    ans.append(sum(i))
for i in range(n):
    if ans[i] == min(ans):
        print(i+1)
        break