input = __import__('sys').stdin.readline
n, *b = (sum(map(int, x.split('+'))) for x in input().rstrip().split('-'))
print(n-sum(b))