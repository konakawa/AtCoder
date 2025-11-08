def solve():
  H, W = map(int, input().split())
  mirrors = []
  for _ in range(H):
    mirrors.append(list(input()))

  L, R, U, D = 0, 1, 2, 3

  out_A = {L: R, R: L, U: D, D: U}
  out_B = {L: D, D: L, R: U, U: R}
  out_C = {L: U, U: L, R: D, D: R}

  mirror_type_and_mapper = [
    ('A', out_A),
    ('B', out_B),
    ('C', out_C),
  ]

  def step(x, y, direction):
    if direction == L:
      return x, y - 1, R
    elif direction == R:
      return x, y + 1, L
    elif direction == U:
      return x - 1, y, D
    elif direction == D:
      return x + 1, y, U

  dist = [[[float('inf')] * 4 for _ in range(W)] for _ in range(H)]
  
  from collections import deque
  dq = deque()

  dist[0][0][L] = 0
  dq.append((0, 0, L))

  ans = float('inf')

  while dq:
    x, y, direction_in = dq.popleft()
    dist_current = dist[x][y][direction_in]
    
    for mirror_type, mapper in mirror_type_and_mapper:
      direction_out = mapper[direction_in]
      weight = 0 if mirrors[x][y] == mirror_type else 1

      if x == H - 1 and y == W - 1 and direction_out == R:
        ans = min(ans, dist_current + weight)
        continue

      next_x, next_y, next_direction = step(x, y, direction_out)
      if not (0 <= next_x < H and 0 <= next_y < W):
        continue

      next_dist = dist_current + weight
      if dist[next_x][next_y][next_direction] > next_dist:
        dist[next_x][next_y][next_direction] = next_dist
        
        if weight == 0:
          dq.appendleft((next_x, next_y, next_direction))
        else:
          dq.append((next_x, next_y, next_direction))

  return ans

T = int(input())
results = []
for _ in range(T):
  results.append(solve())

for result in results:
  print(result)