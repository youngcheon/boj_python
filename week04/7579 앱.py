input = __import__('sys').stdin.readline
n, m = map(int,input().split())
a,c = list(map(int, input().split())), list(map(int, input().split()))
s = sum(c)
dp = [0]*(s+1)
for memory, cost in zip(a, c):
    for i in range(s, cost-1, -1):
        if i < cost:
            break
        dp[i] = max(dp[i], dp[i-cost]+memory)
for i in range(s+1):
    if dp[i] >= m:
        print(i)
        break