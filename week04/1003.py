input = __import__('sys').stdin.readline

t = int(input())
dp = [(1,0),(0,1)] + [(0,0)]*40
for _ in range(t):
    n = int(input())
    for i in range(2, n+1):
        a = dp[i-1]
        b = dp[i-2]
        dp[i] = (a[0]+b[0],a[1]+b[1])
    print(*dp[n])