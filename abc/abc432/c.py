N, X, Y = map(int, input().split())
As = list(map(int, input().split()))

diff = Y - X

# W[i] = X * (A[i] - num_y) + Y * num_y
# W[i] = X * A[i] + (Y - X) * num_y
# W[i] = X * A[i] + diff * num_y
# W[i] ≡ X * A[i] (mod diff)

W_mod = X * As[0] % diff
for i in range(1, N):
  if W_mod != X * As[i] % diff:
    print("-1")
    exit()

limit_min = max(X*As[i] for i in range(N))
limit_max = min(Y*As[i] for i in range(N))

if limit_min > limit_max:
  print("-1")
  exit()

W = limit_max - ((limit_max - W_mod) % diff)

sum_num_y = sum((W - X * As[i]) // diff for i in range(N))

print(sum_num_y)