N = int(input())
rabbits = [list(map(int, input().split())) for _ in range(N)] # [(X, R), ...]

coordinates = set()
for x, r in rabbits:
  coordinates.add(x - r)
  coordinates.add(x + r)

coordinates_to_idx = {coordinate: i for i, coordinate in enumerate(coordinates)}
V = len(coordinates)

parent = list(range(V))

def find(x):
  root = x
  while parent[root] != root:
    root = parent[root]
  
  while parent[x] != root:
    next = parent[x]
    parent[x] = root
    x = next
  
  return root

def union(x, y):
  px, py = find(x), find(y)
  if px != py:
    parent[py] = px

for x, r in rabbits:
  u = coordinates_to_idx[x - r]
  v = coordinates_to_idx[x + r]
  union(u, v)

from collections import defaultdict
vertex_count = defaultdict(int)
edge_count = defaultdict(int)

for i in range(V):
  vertex_count[find(i)] += 1

for x, r in rabbits:
  u = coordinates_to_idx[x - r]
  edge_count[find(u)] += 1

tree_count = sum(1 for root in vertex_count if edge_count[root] == vertex_count[root] - 1)

print(V - tree_count)