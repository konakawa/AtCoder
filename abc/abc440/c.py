def solve():
  N, W = map(int, input().split())
  Cs = list(map(int, input().split()))

  cost_grouped_by_mod = [0] * (2 * W)
  for i in range(N):
    j = (i + 1) % (2 * W)
    cost_grouped_by_mod[j] += Cs[i]

  current_sum = sum(cost_grouped_by_mod[:W])
  min_sum = current_sum
  
  for j in range(2 * W - 1):
    current_sum += cost_grouped_by_mod[(j + W) % (2 * W)] - cost_grouped_by_mod[j]
    min_sum = min(min_sum, current_sum)

  print(min_sum)

T = int(input())
for _ in range(T):
  solve()