N, M = map(int, input().split())
edges = []
for _ in range(M):
  X, Y = map(int, input().split())
  edges.append((X, Y))

graph = [[] for _ in range(N + 1)]
for X, Y in edges:
  graph[X].append(Y)

reverse_graph = [[] for _ in range(N + 1)]
for X, Y in edges:
  reverse_graph[Y].append(X)

Q = int(input())

reachable_from_black = set()

from collections import deque
def add_black(v):
  if v in reachable_from_black:
    return
  
  queue = deque([v])
  while queue:
    u = queue.popleft()
    if u in reachable_from_black:
      continue
    reachable_from_black.add(u)
    for w in reverse_graph[u]:
      if w not in reachable_from_black:
        queue.append(w)

for _ in range(Q):
  q, v = map(int, input().split())

  if q == 1:
    add_black(v)
  else:
    if v in reachable_from_black:
      print("Yes")
    else:
      print("No")