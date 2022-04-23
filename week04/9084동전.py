input = __import__('sys').stdin.readline

for _ in range(int(input())):
    n = int(input())
    coins = list(map(int,input().split()))
    target = int(input())
    dp = [1]+[0]*target
    
    for c in coins:
        for i in range(target+1):
            if i >= c:
                dp[i] += dp[i-c]
    print(dp[target])