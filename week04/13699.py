dp=[1,1,2]+[0]*33
n=int(input())
for i in range(3,n+1):
    for j in range(i):
        dp[i] += dp[j]*dp[i-j-1]
print(dp[n])