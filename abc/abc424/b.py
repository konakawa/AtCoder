N, M, K = map(int, input().split())

from collections import defaultdict
counts = defaultdict(int)

results = []
for _ in range(K):
  A, B = map(int, input().split())
  counts[A] += 1
  if counts[A] == M:
    results.append(A)

if len(results):
  print(" ".join(map(str, results)))
