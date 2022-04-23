input = __import__('sys').stdin.readline

word1, word2 = input().rstrip(), input().rstrip()
l1, l2 = len(word1), len(word2)
dp = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < dp[j]:
            cnt = dp[j]
        elif word1[i] == word2[j]:
            dp[j] = cnt + 1
print(max(dp))