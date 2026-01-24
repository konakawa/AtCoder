N, M = map(int, input().split())

relation_counts = [0] * N

for _ in range(M):
  A, B = map(int, input().split())
  relation_counts[A - 1] += 1
  relation_counts[B - 1] += 1

results = []
for i in range(N):
  n = N - 1 - relation_counts[i]
  result = n * (n - 1) * (n - 2) // 6
  results.append(result)

print(" ".join(map(str, results)))