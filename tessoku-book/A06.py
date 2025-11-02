N, Q = map(int, input().split())
As = list(map(int, input().split()))

prefix_sums = [0]
for i in range(N):
  prefix_sums.append(prefix_sums[-1] + As[i])

results = []
for _ in range(Q):
  L, R = map(int, input().split())
  results.append(prefix_sums[R] - prefix_sums[L - 1])

for result in results:
  print(result)