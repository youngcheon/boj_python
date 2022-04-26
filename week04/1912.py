input = __import__('sys').stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
dp = [numbers[0]]+[0]*(n-1)
for i in range(n):
    dp[i] = max(dp[i-1]+numbers[i], numbers[i])
print(max(dp))