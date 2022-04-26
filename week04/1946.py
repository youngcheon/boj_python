input = __import__('sys').stdin.readline
for _ in range(int(input())):
    n = int(input())
    array = sorted([tuple(map(int,input().split())) for _ in range(n)])
    temp = array[0][1]
    count = 1
    for i in range(n):
        rank = array[i][1]
        if rank < temp:
            temp = rank
            count += 1
    print(count)