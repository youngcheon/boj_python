#https://www.acmicpc.net/problem/11722
input = __import__('sys').stdin.readline
n = int(input())
li = list(map(int, input().split()))
dp = [1]*(n)
for i in range(n):  
    for j in range(i):
        if li[j] > li[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))