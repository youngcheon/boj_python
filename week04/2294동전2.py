input = __import__('sys').stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
