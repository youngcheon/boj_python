input = __import__('sys').stdin.readline
from collections import deque
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    cost = [0]+list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    d = [0]*(n+1)
    dp = [0]*(n+1)
    result = []
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        d[b] += 1
    w = int(input())
    q = deque()
    for i in range(1, n+1):
        if not d[i]:
            q.append(i)
            dp[i] = cost[i]
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            d[i] -= 1
            dp[i] = max(dp[now]+cost[i], dp[i])
            if d[i] == 0:
                q.append(i)
    print(dp[w])