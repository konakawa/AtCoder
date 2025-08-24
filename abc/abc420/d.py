H, W = map(int, input().split())
grid = []
for _ in range(H):
  grid.append(list(input()))

switched_grid = []
for i in range(H):
  row = []
  for j in range(W):
    if grid[i][j] == 'o':
      row.append('x')
    elif grid[i][j] == 'x':
      row.append('o')
    else:
      row.append(grid[i][j])
  switched_grid.append(row)

for i in range(H):
  for j in range(W):
    if grid[i][j] == 'S':
      sx, sy = i, j
    elif grid[i][j] == 'G':
      gx, gy = i, j

INF = 10 ** 9
dist = [[[INF] * 2 for _ in range(W)] for _ in range(H)]
dist[sx][sy][0] = 0

from collections import deque

q = deque()
q.append((sx, sy, 0))

def passable(c):
  return c != '#' and c != 'x'

while q:
  x, y, p = q.popleft()
  d = dist[x][y][p]

  for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    nx, ny = x + dx, y + dy
    if 0 <= nx < H and 0 <= ny < W:
      next_grid = grid if p == 0 else switched_grid
      if passable(next_grid[nx][ny]):
        np = p ^ 1 if next_grid[nx][ny] == '?' else p
        if dist[nx][ny][np] > d + 1:
          dist[nx][ny][np] = d + 1
          q.append((nx, ny, np))

ans = min(dist[gx][gy])
print(ans if ans != INF else -1)
