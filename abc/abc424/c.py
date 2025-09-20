N = int(input())
Nodes = []

for _ in range(N):
  A, B = map(int, input().split())
  Nodes.append((A, B))

rev_graph = [[] for _ in range(N+1)]
mastered = []
for i in range(N):
  A, B = Nodes[i]
  if A == 0 and B == 0:
    mastered.append(i)
  else:
    rev_graph[A-1].append(i)
    rev_graph[B-1].append(i)

from collections import deque
dq = deque(mastered)
visited = [False] * N

for node in mastered:
  visited[node] = True

while dq:
  node = dq.popleft()
  for next_node in rev_graph[node]:
    if not visited[next_node]:
      visited[next_node] = True
      dq.append(next_node)

print(sum(visited))