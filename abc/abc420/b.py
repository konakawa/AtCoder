N, M = map(int, input().split())

Ss = []
for _ in range(N):
  Ss.append(list(map(int, input().strip())))

points = [0] * N

winners = []

for j in range(M):
  count_0 = 0
  for i in range(N):
    if Ss[i][j] == 0:
      count_0 += 1
  if count_0 > N // 2:
    winners.append(1)
  else:
    winners.append(0)

win_counts = [0] * N

for i in range(N):
  for j in range(M):
    if Ss[i][j] == winners[j]:
      win_counts[i] += 1

max_win_count = max(win_counts)

results = []

for i in range(N):
  if win_counts[i] == max_win_count:
    results.append(i + 1)

print(" ".join(map(str, results)))