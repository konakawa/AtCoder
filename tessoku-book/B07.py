T = int(input())
N = int(input())

diffs = [0] * (T + 1)
for _ in range(N):
  L, R = map(int, input().split())
  diffs[L] += 1
  diffs[R] -= 1

prefix_sums = [0]
for i in range(T):
  prefix_sums.append(prefix_sums[-1] + diffs[i])

for i in range(1, T + 1):
  print(prefix_sums[i])