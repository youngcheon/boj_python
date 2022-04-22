#https://www.acmicpc.net/problem/1149
input = __import__('sys').stdin.readline

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(3):
        a, b, c = dp[i-1]
        dp[i][j] += {0: min(b,c), 1: min(a,c), 2: min(a,b)}[j]
print(min(dp[-1]))
