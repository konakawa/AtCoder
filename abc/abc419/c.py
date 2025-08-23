N = int(input())

positions = []
for _ in range(N):
  r, c = map(int, input().split())
  positions.append((r, c))

positions_sorted_by_r = sorted(positions, key=lambda x: x[0])
positions_sorted_by_c = sorted(positions, key=lambda x: x[1])

max_r_diff = positions_sorted_by_r[-1][0] - positions_sorted_by_r[0][0]
max_c_diff = positions_sorted_by_c[-1][1] - positions_sorted_by_c[0][1]

result = (max(max_r_diff, max_c_diff) + 1) // 2

print(result)