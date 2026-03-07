import sys
sys.setrecursionlimit(10**6)

N = int(input())
As = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for i in range(N - 1):
  U, V = map(int, input().split())
  graph[U - 1].append(V - 1)
  graph[V - 1].append(U - 1)

ans = [False] * N
value_counts = {}
pair_count = 0

def dfs(current, parent):
  global pair_count

  value = As[current]
  old_count = value_counts.get(value, 0)

  pair_count += old_count
  value_counts[value] = old_count + 1

  ans[current] = pair_count > 0

  for next in graph[current]:
    if next == parent:
      continue
    dfs(next, current)

  value_counts[value] -= 1
  pair_count -= value_counts[value]

  if value_counts[value] == 0:
    del value_counts[value]

dfs(0, -1)

for a in ans:
  print("Yes" if a else "No")