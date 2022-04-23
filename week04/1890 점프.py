input = __import__('sys').stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n-1 and j==n-1:
            print(dp[i][j])
            break
        count = graph[i][j]
        if j + count < n:
            dp[i][j+count] += dp[i][j]
        if i + count < n :
            dp[i+count][j] += dp[i][j]