N = int(input())
edges = []
for _ in range(N - 1):
  a, b = map(int, input().split())
  edges.append((a, b))

graph = [[] for _ in range(N)]
for a, b in edges:
  graph[a - 1].append(b - 1)
  graph[b - 1].append(a - 1)

from collections import deque

dist_from_0 = [-1] * N
dist_from_0[0] = 0
queue = deque([0])
while queue:
  v = queue.popleft()
  for u in graph[v]:
    if dist_from_0[u] == -1:
      dist_from_0[u] = dist_from_0[v] + 1
      queue.append(u)

max_dist = max(dist_from_0)
furthest_vertex = dist_from_0.index(max_dist)

dist_from_furthest = [-1] * N
dist_from_furthest[furthest_vertex] = 0
queue = deque([furthest_vertex])
while queue:
  v = queue.popleft()
  for u in graph[v]:
    if dist_from_furthest[u] == -1:
      dist_from_furthest[u] = dist_from_furthest[v] + 1
      queue.append(u)

print(max(dist_from_furthest) + 1)