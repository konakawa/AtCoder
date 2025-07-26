def check():
  N, M = map(int, input().split())
  As = list(map(int, input().split()))
  Bs = list(map(int, input().split()))

  over_M_pairs_count = 0
  i = 0
  j = N - 1

  As.sort()
  Bs.sort()

  while i < N and j >= 0:
    if As[i] + Bs[j] >= M:
      over_M_pairs_count += 1
      i += 1
      j -= 1
    else:
      i += 1
      
  return sum(As) + sum(Bs) - over_M_pairs_count * M

T = int(input())

results = []
for _ in range(T):
  results.append(check())

for result in results:
  print(result)
