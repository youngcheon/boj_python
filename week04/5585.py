coins = [500,100,50,10,5,1]
n = 1000-int(input())
count = 0
for i in coins:
    count += n // i
    n %= i
print(count)