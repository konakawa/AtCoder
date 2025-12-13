from collections import deque, defaultdict

H, W = map(int, input().split())

grid = []
grid = [list(input()) for _ in range(H)]

warps = defaultdict(list)
for i in range(H):
  for j in range(W):
    c = grid[i][j]
    if 'a' <= c <= 'z':
      warps[c].append((i, j))

start = (0, 0)
goal = (H - 1, W - 1)

dist = [[float('inf')] * W for _ in range(H)]
dist[0][0] = 0

q = deque([start])
used_warp = set()

while q:
  r, c = q.popleft()

  if (r, c) == goal:
    print(dist[r][c])
    exit()

  for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    nr, nc = r + dr, c + dc
    if 0 <= nr < H and 0 <= nc < W:
      if grid[nr][nc] != '#' and dist[nr][nc] == float('inf'):
        dist[nr][nc] = dist[r][c] + 1
        q.append((nr, nc))

  ch = grid[r][c]
  if 'a' <= ch <= 'z' and ch not in used_warp:
    used_warp.add(ch)
    for nr, nc in warps[ch]:
      if dist[nr][nc] == float('inf'):
        dist[nr][nc] = dist[r][c] + 1
        q.append((nr, nc))

print(-1)