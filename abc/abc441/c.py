N, K, X = map(int, input().split())
As = list(map(int, input().split()))

As.sort()


alcohol_sum = 0
for i in range(K):
  alcohol_sum += As[K - 1 - i]
  if alcohol_sum >= X:
    print(N - K + i + 1)
    exit()

print(-1)