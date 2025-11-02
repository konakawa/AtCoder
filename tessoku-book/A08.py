H, W = map(int, input().split())
grid = []

for _ in range(H):
  grid.append(list(map(int, input().split())))

prefix_sums = [[0] * (W + 1) for _ in range(H + 1)]

# 行方向の累積和
for i in range(1, H + 1):
  running = 0
  row = grid[i - 1]
  for j in range(1, W + 1):
    running += row[j - 1]
    prefix_sums[i][j] = running

# 列方向の累積和
for j in range(1, W + 1):
  running = 0
  for i in range(1, H + 1):
    running += prefix_sums[i][j]
    prefix_sums[i][j] = running

Q = int(input())

results = []
for _ in range(Q):
  A, B, C, D = map(int, input().split())
  results.append(prefix_sums[C][D] - prefix_sums[A - 1][D] - prefix_sums[C][B - 1] + prefix_sums[A - 1][B - 1])

for result in results:
  print(result)