input = __import__('sys').stdin.readline
n, k = map(int, input().split())
l = sorted([list(map(int, input().split())) for _ in range(n)])
dp = [0]*(k+1)
for w,v in l:
    for i in range(k, w-1, -1):
        if i<w: 
            break
        dp[i] = max(dp[i], dp[i-w]+v)
print(dp.pop())