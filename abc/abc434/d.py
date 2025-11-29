N = int(input())
clouds = [list(map(int, input().split())) for _ in range(N)]

H = 2000
W = 2000

counts = [[0] * (W + 1) for _ in range(H + 1)]
sun_idx = [[0] * (W + 1) for _ in range(H + 1)]

for i, (U, D, L, R) in enumerate(clouds):
  idx = i + 1

  counts[U - 1][L - 1] += 1
  counts[U - 1][R] -= 1
  counts[D][L - 1] -= 1
  counts[D][R] += 1

  sun_idx[U - 1][L - 1] += idx
  sun_idx[U - 1][R] -= idx
  sun_idx[D][L - 1] -= idx
  sun_idx[D][R] += idx

for r in range(H):
  for c in range(W):
    counts[r][c + 1] += counts[r][c]
    sun_idx[r][c + 1] += sun_idx[r][c]

for c in range(W):
  for r in range(H):
    counts[r + 1][c] += counts[r][c]
    sun_idx[r + 1][c] += sun_idx[r][c]

alone = [0] * (N + 1)
uncovered = 0

for r in range(H):
  for c in range(W):
    count = counts[r][c]
    if count == 0:
      uncovered += 1
    elif count == 1:
      alone[sun_idx[r][c]] += 1

for i in range(1, N + 1):
  print(uncovered + alone[i])