N = int(input())
Ws = []
Hs = []
Bs = []
for _ in range(N):
  W, H, B = map(int, input().split())
  Ws.append(W)
  Hs.append(H)
  Bs.append(B)

base = sum(Bs)
max_head_weight = sum(Ws) // 2

dp = [float('-inf')] * (max_head_weight + 1)
dp[0] = 0

for i in range(N):
  for j in range(max_head_weight, Ws[i] - 1, -1):
    dp[j] = max(dp[j], dp[j - Ws[i]] + Hs[i] - Bs[i])

best = max(dp)
print(best + base)