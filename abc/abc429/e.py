N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
  u, v = map(int, input().split())
  graph[u - 1].append(v - 1)
  graph[v - 1].append(u - 1)
S = list(input())

from collections import deque

best = [[] for _ in range(N)]

q = deque()
for i in range(N):
  if S[i] == 'S':
    q.append(i)
    best[i].append((0, i))

while q:
  u = q.popleft()
  for v in graph[u]:
    pushed = False
    for dist_u, source_u in best[u]:
      new_dist = dist_u + 1

      same_idx = -1
      for i, (dist_v, source_v) in enumerate(best[v]):
        if source_v == source_u:
          same_idx = i
          break

      if same_idx == -1:
        if len(best[v]) < 2:
          best[v].append((new_dist, source_u))
          pushed = True
        else:
          best[v].sort()
          if new_dist < best[v][1][0]:
            best[v][1] = (new_dist, source_u)
            pushed = True
      else:
        if new_dist < best[v][same_idx][0]:
          best[v][same_idx] = (new_dist, source_u)
          pushed = True

    if pushed:
      best[v].sort()
      q.append(v)

for i in range(N):
  if S[i] == 'D' and len(best[i]) >= 2:
    (dist_1, source_1), (dist_2, source_2) = best[i][0], best[i][1]
    if source_1 != source_2:
      print(dist_1 + dist_2)