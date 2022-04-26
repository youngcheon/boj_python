input = __import__('sys').stdin.readline
n, m = map(int, input().split())
set6, one = 1000, 1000
for _ in range(m):
    a, b = map(int,input().split())
    set6 = min(set6, a)
    one = min(one, b)
print(min(set6*((n//6)+1), set6*(n//6)+one*(n%6), one*n))