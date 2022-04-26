a = list(input().split())
print(sum(map(lambda x: int(x.replace('6','5')), a)), end=' ')
print(sum(map(lambda x: int(x.replace('5','6')), a)))