#https://www.acmicpc.net/problem/1149
input = __import__('sys').stdin.readline
n = int(input())
s = [int(input()) for _ in range(n)]
s.insert(0, 0)
if n == 1:
    print(s[1])
else:
    dp = [0]*(n+1)
    dp[1] = s[1]
    dp[2] = s[1]+s[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+s[i-1]+s[i],dp[i-2]+s[i])
    print(dp.pop())