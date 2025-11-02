N = int(input())

points = []
for _ in range(N):
  x, y = map(int, input().split())
  points.append((x, y))

grid = [[0] * 1501 for _ in range(1501)]

for x, y in points:
  grid[x][y] += 1

prefix_sums = [[0] * 1501 for _ in range(1501)]

for i in range(1501):
  for j in range(1501):
    prefix_sums[i][j] = grid[i][j] + prefix_sums[i - 1][j] + prefix_sums[i][j - 1] - prefix_sums[i - 1][j - 1]

Q = int(input())

results = []
for _ in range(Q):
  a, b, c, d = map(int, input().split())
  print(prefix_sums[c][d] - prefix_sums[a - 1][d] - prefix_sums[c][b - 1] + prefix_sums[a - 1][b - 1])

for result in results:
  print(result)