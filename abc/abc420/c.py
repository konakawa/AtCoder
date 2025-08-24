N, Q = map(int, input().split())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

current = 0
for i in range(N):
  current += min(As[i], Bs[i])

for i in range(Q):
  c, X, V = input().split()
  X, V = int(X), int(V)

  target_value = min(As[X - 1], Bs[X - 1])

  if c == 'A':
    As[X - 1] = V
  else:
    Bs[X - 1] = V

  replacing_value = min(As[X - 1], Bs[X - 1])

  current += replacing_value - target_value

  print(current)