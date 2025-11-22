N = int(input())
As = list(map(int, input().split()))

for i in range(N):
  diff = float('inf')
  base = As[i]
  idx = -1
  for j in range(i):
    if As[j] > base:
      diff = min(diff, As[j] - base)
      idx = j + 1  
  print(idx)