#https://www.acmicpc.net/problem/1932
input = __import__('sys').stdin.readline
n = int(input())
dp= []
for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1,n): # 층 
    for j in range(len(dp[i])): # 층의 숫자들
        if j == 0:
            # 첫번째일경우 바로 위에 숫자 더함
            dp[i][j] += dp[i-1][j]
        elif j == len(dp[i])-1:
            # 마지막 숫자일경우 바로 위에 숫자 더함
            dp[i][j] += dp[i-1][j-1]
        else:
            # 나머지는 위에있는 두 숫자중에 큰 값을 더함
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[-1]))