N = int(input())

grid = [[0] * (1502) for _ in range(1502)]

for _ in range(N):
  A, B, C, D = map(int, input().split())
  grid[A + 1][B + 1] += 1
  grid[A + 1][D + 1] -= 1
  grid[C + 1][B + 1] -= 1
  grid[C + 1][D + 1] += 1

for i in range(1, 1502):
  for j in range(1, 1502):
    grid[i][j] += grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1]

count = 0
for i in range(1502):
  for j in range(1502):
    if grid[i][j] > 0:
      count += 1

print(count)