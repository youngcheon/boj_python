# https://www.acmicpc.net/problem/9461
input = __import__('sys').stdin.readline
dp = [1,1,1,2,2]+[0]*100
for i in range(5, 100):
    dp[i] = dp[i-1]+dp[i-5]
for _ in range(int(input())):
    n = int(input())
    print(dp[n-1])