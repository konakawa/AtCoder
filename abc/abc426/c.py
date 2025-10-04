N, Q = map(int, input().split())

lower_limit = 1

PCs = {i: 1 for i in range(1, N + 1)}

for _ in range(Q):
  X, Y = map(int, input().split())
  
  if X < lower_limit:
    print(0)
    continue
  
  count = 0
  for i in range(lower_limit, X+1):
    count += PCs[i]
    PCs[i] = 0

  lower_limit = X + 1
  PCs[Y] += count

  print(count)