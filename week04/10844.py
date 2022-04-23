#https://www.acmicpc.net/problem/10844
input = __import__('sys').stdin.readline
n = int(input())
drink = [0]*10000
for i in range(n):
    drink[i] = int(input())
dp = [0]*10000
dp[0] = (drink[0])
dp[1] = (drink[0]+drink[1])
dp[2] = (max(drink[2]+drink[0], drink[2]+drink[1], dp[1]))
for i in range(3, n):
    dp[i] = max(drink[i]+dp[i-2], drink[i]+drink[i-1]+dp[i-3], dp[i-1])
print(max(dp))