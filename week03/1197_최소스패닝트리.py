# https://www.acmicpc.net/problem/1197

# 크루스칼 알고리즘
from sys import stdin 
input = stdin.readline

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트노드가 아니라면, 루트노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split()) 
parent = [0]*(v+1)  # 부모테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선의 정보를 입력받기
for _ in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))
# 간선을 cost 순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며, 사이클이 발생하지 않는 경우에만 집합에 포함
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

# prim 알고리즘
# import sys
# import heapq
# input = sys.stdin.readline
 
# V, E = map(int, input().split())
# visited = [False]*(V+1)
# Elist = [[] for _ in range(V+1)]
# heap = [[0, 1]]
# for _ in range(E):
#     s, e, w = map(int, input().split())
#     Elist[s].append([w, e])
#     Elist[e].append([w, s])
 
# answer = 0
# cnt = 0
# while heap:
#     if cnt == V:
#         break
#     w, s = heapq.heappop(heap)
#     if not visited[s]:
#         visited[s] = True
#         answer += w
#         cnt += 1
#         for i in Elist[s]:
#             heapq.heappush(heap, i)
 
# print(answer)