from collections import defaultdict

H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

visited = set()
for i in range(H):
  for j in range(W):
    if grid[i][j] == '#':
      visited.add((i, j))


dirs = [(1,0), (-1,0), (0,1), (0,-1)]

front = list(visited)

blocked = set()

while front:
  inc = defaultdict(int)
  for x, y in front:
    for dx, dy in dirs:
      nx, ny = x + dx, y + dy
      if 0 <= nx < H and 0 <= ny < W:
        v = (nx, ny)
        if v in visited or v in blocked:
          continue
        inc[v] += 1

  next_front = []
  for v, c in inc.items():
    if c == 1:
      visited.add(v)
      next_front.append(v)
    else:
      blocked.add(v)

  front = next_front

print(len(visited))