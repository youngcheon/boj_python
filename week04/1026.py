input = __import__('sys').stdin.readline
_ = input()
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
print(sum((i*j) for i,j in zip(a,reversed(b))))