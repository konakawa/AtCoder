N, M, L = map(int, input().split())
As = list(map(int, input().split()))

dp = [[float('inf')] * M for _ in range(L)]

costs = [[0] * M for _ in range(L)]

for i in range(L):
  mod_occurrences = [0] * M
  tmp = i
  while tmp < N:
    mod = As[tmp] % M
    mod_occurrences[mod] += 1
    tmp += L

  for j in range(M):
    for k in range(M):
      costs[i][j] += mod_occurrences[k] * ((j - k) % M)

for j in range(M):
  dp[0][j] = costs[0][j]

for i in range(1, L):
  for j in range(M):
    for k in range(M):
      diff = (j - k) % M
      dp[i][j] = min(dp[i][j], dp[i - 1][k] + costs[i][diff])

print(dp[L - 1][0])