input = __import__('sys').stdin.readline
from heapq import heappush, heappop
n, k = map(int, input().split())
heap = []
bosuck = sorted([list(map(int, input().split())) for _ in range(n)])
bags = sorted([int(input()) for _ in range(k)])
result = 0
temp = []
for bag in bags:
    while bosuck and bag >= bosuck[0][0]:
        heappush(temp, -bosuck[0][1])
        heappop(bosuck)
    if temp:
        result += heappop(temp)
    elif not bosuck:
        break
print(-result)