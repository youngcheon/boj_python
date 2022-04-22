#https://www.acmicpc.net/problem/9095
input = __import__('sys').stdin.readline
dp = [1,1,2]
for i in range(3,12):
    dp.append(sum(dp[-3:]))
for _ in range(int(input())):
    print(dp[int(input())])
    