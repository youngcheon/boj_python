input = __import__('sys').stdin.readline
li = []
for _ in range(int(input())):
    li.append(tuple(map(int, input().split())))
li.sort(key=lambda x: (x[1],x[0]))
start, end = li[0]
count = 1
for i in range(1,len(li)):
    s, e = li[i]
    if s >= end:
        count += 1
        start = s
        end = e
print(count)