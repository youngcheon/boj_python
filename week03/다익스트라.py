from heapq import heappush,heappop
import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
distance = [INF]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
start, end = map(int, input().split())
q = []
heappush(q, (0, start))
distance[start] = 0
while q:
    # 최단거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heappop(q)
    # 이미 처리된 노드였다면 무시
    if distance[now] < dist:
        continue
    # 선택된 노드와 인접한 노드를 확인
    for i in graph[now]:
        # i[0] = 목적지 / i[1] = 비용
        cost = dist + i[1] 
        # 선택된 노드를 거쳐서 이동하는 것이 빠를 경우
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heappush(q, (cost,i[0]))
print(distance[end])


