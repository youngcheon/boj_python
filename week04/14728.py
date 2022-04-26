input = __import__('sys').stdin.readline
n, t = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
li.sort()
dp = [0]*(t+1)
for k, s in li:
    for i in range(t, k-1, -1):
        if i<k:
            break
        dp[i] = max(dp[i], dp[i-k]+s)
print(dp.pop())