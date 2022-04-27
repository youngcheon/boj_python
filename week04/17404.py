input = __import__('sys').stdin.readline
from math import inf
n=int(input())
house = [list(map(int,input().split())) for _ in range(n)]
result = inf
for start in range(3):
    dp=[[0]*3 for _ in range(n)]
    for i in range(3):
        dp[0][i] = house[0][i] if i==start else inf
    for i in range(1, n):
        for j in range(3):
            r,g,b=dp[i-1]
            dp[i][j] = house[i][j]+{0:min(g,b),1:min(r,b),2:min(r,g)}[j]
    for i in range(3):
        if i!=start:
            result = min(result, dp[-1][i])    
print(result)