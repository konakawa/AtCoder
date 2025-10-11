N, M = map(int, input().split())

edges = []
for _ in range(M):
  u, v = map(int, input().split())
  edges.append((u, v))

max = 0
for i in range(2**N):
  count = 0
  for u, v in edges:
    if (i >> (u - 1)) & 1 ^ (i >> (v - 1)) & 1:
      count += 1
  if count > max:
    max = count

print(M - max)