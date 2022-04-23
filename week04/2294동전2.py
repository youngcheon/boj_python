input = __import__('sys').stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [1]+[0]*k
for c in coins:
    for i in range(k+1):
        if i>=c:
            dp[i] += dp[i-c]
print(dp[k])