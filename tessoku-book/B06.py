N = int(input())
As = list(map(int, input().split()))
Q = int(input())

prefix_sums = [0]
for i in range(N):
  prefix_sums.append(prefix_sums[-1] + As[i])

results = []
for _ in range(Q):
  L, R = map(int, input().split())
  diff = R - L + 1
  hits = prefix_sums[R] - prefix_sums[L - 1]
  if hits == diff / 2:
    results.append('draw')
  elif hits > diff / 2:
    results.append('win')
  else:
    results.append('lose')

for result in results:
  print(result)