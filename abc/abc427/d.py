def solve():
  N, M, K = map(int, input().split())
  S = list(input())
  edges = []
  for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))

  graph = [[] for _ in range(N)]
  for u, v in edges:
    graph[u - 1].append(v - 1)

  DP_A = [[False] * N for _ in range(2 * K + 1)] # DP_A[t][v] := A の手番で 残り t 手・現在位置 v から A が勝利するか
  DP_B = [[False] * N for _ in range(2 * K + 1)] # DP_B[t][v] := B の手番で 残り t 手・現在位置 v から A が勝利するか

  for v in range(N):
    DP_A[0][v] = (S[v] == 'A')
    DP_B[0][v] = (S[v] == 'A')

  for t in range(1, 2 * K + 1):
    for v in range(N):
      can_reach_A = False
      for u in graph[v]:
        if DP_B[t - 1][u]:
          can_reach_A = True
          break
      DP_A[t][v] = can_reach_A

    for v in range(N):
      can_reach_A = True
      for u in graph[v]:
        if not DP_A[t - 1][u]:
          can_reach_A = False
          break
      DP_B[t][v] = can_reach_A

  return 'Alice' if DP_A[2 * K][0] else 'Bob'

T = int(input())

results = []
for _ in range(T):
  results.append(solve())

for result in results:
  print(result)