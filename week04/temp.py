input = __import__('sys').stdin.readline
d = [0]*3
n = int(input())
for x in zip(map(int,input().split())):
    print(x)
    # r, g, b = map(int, input().split())
    # d1, d2, d3 = d
    # d = [min(d2,d3)+r,min(d1,d3)+g,min(d1,d2)+b]
print(min(d))