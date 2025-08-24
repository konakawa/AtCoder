H, W = map(int, input().split())

grid = []
for _ in range(H):
  grid.append(list(map(int, input().split())))

H_sums = [0] * W
for i in range(H):
  for j in range(W):
    H_sums[j] += grid[i][j]

W_sums = [0] * H
for i in range(H):
  W_sums[i] = sum(grid[i])

for i in range(H):
  for j in range(W):
    if j == W - 1:
      print(H_sums[j] + W_sums[i] - grid[i][j])
    else:
      print(H_sums[j] + W_sums[i] - grid[i][j], end=" ")