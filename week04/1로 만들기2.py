input = __import__('sys').stdin.readline
from collections import deque
def solve(x):
    q = deque()
    q.append([x])
    result = []
    while q:
        a = q.popleft()
        x = a[0]
        if x == 1:
            result = a
            break
        if x % 3 == 0:
            q.append([x//3]+a)
        if x % 2 == 0:
            q.append([x//2]+a)
        q.append([x-1]+a)
    return len(result)-1, result[::-1]
x = int(input())
answer = solve(x)
print(str(answer[0])+'\n'+' '.join(map(str, answer[1])))