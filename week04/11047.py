input = __import__('sys').stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)][::-1]
count = 0
for i in coins:
    count += k//i
    k %= i
print(count)
