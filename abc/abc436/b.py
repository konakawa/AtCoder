N = int(input())

grid = [[0] * N for _ in range(N)]

def next(r, c, k):
  nr = (r - 1) % N
  nc = (c + 1) % N
  
  if grid[nr][nc] == 0:
    return nr, nc, k + 1
  else:
    nr = (r + 1) % N
    nc = c
    return nr, nc, k + 1

r, c = 0, (N - 1) // 2
k = 1
grid[r][c] = k

for _ in range(N ** 2 - 1):
  nr, nc, nk = next(r, c, k)
  grid[nr][nc] = nk
  r, c, k = nr, nc, nk

for row in grid:
  print(' '.join(map(str, row)))