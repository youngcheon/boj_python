input = __import__('sys').stdin.readline

n = int(input())
dp = [0,1,2]+[0]*1000000
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746
print(dp[n])