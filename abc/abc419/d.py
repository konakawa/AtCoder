N, M = map(int, input().split())
S = list(input())
T = list(input())

trade_counts = [0] * (N + 1)

for _ in range(M):
  L, R = map(int, input().split())
  trade_counts[L - 1] += 1
  trade_counts[R] -= 1

for i in range(1, N + 1):
  trade_counts[i] += trade_counts[i - 1]

for i in range(N):
  if trade_counts[i] % 2 == 1:
    S[i], T[i] = T[i], S[i]

print(''.join(S))