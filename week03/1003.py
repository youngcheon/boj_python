input = __import__('sys').stdin.readline
t = int(input())
dp = [0,1]+[0]*40
for _ in range(t):
    n = int(input())
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    print(dp[n])