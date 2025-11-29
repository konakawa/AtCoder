N, M = map(int, input().split())
ABs = [list(map(int, input().split())) for _ in range(N)]

for i in range(M):
  count  = 0
  weight = 0
  for j in range(N):
    if ABs[j][0] == i + 1:
      count += 1
      weight += ABs[j][1]
  print(weight / count)