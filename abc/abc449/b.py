H, W, Q = map(int, input().split())

for _ in range(Q):
  q, n = map(int, input().split())

  if q == 1:
    print(n * W)
    H -= n
  else:
    print(n * H)
    W -= n