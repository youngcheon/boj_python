#https://www.acmicpc.net/problem/11726
input = __import__('sys').stdin.readline
dp = [0,1]
n = int(input())
if n > 1:
    dp.append(2)
    for i in range(3, n+1):
        dp.append(sum(dp[-2:])%10007)
print(dp.pop())
