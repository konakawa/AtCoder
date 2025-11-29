def solve():
  N, H = map(int, input().split())
  targets = [list(map(int, input().split())) for _ in range(N)]

  targets.sort(key=lambda x: x[0])

  t_current = 0
  h_current_l = H
  h_current_u = H

  for target in targets:
    t, l, u = target
    t_diff = t - t_current

    h_next_l = max(0, h_current_l - t_diff)
    h_next_u = h_current_u + t_diff

    if h_next_l > u or h_next_u < l:
      return "No"

    h_intersect_l = max(h_next_l, l)
    h_intersect_u = min(h_next_u, u)

    h_current_l = h_intersect_l
    h_current_u = h_intersect_u

    t_current = t

  return "Yes"

T = int(input())
results = []
for _ in range(T):
  results.append(solve())

for result in results:
  print(result)