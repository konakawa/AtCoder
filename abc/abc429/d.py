N, M, C = map(int, input().split())
As = list(map(int, input().split()))

from collections import Counter
c = Counter(As)
positions = sorted(c.keys())
counts = [c[p] for p in positions]
n = len(positions)

prefix_sums = [0]
for count in counts:
  prefix_sums.append(prefix_sums[-1] + count)

prefix_sums_double = prefix_sums[1:] + [prefix_sums[-1] + x for x in prefix_sums[1:]]

result = 0

from bisect import bisect_left

for i in range(n):
  current_position = positions[i]
  prev_position = positions[i - 1] if i > 0 else positions[-1]
  L = current_position - prev_position if i > 0 else current_position + M - prev_position
  if L == 0:
    continue

  base = prefix_sums[i]
  target = base + C

  j = bisect_left(prefix_sums_double, target, i, i + n)
  
  passed_count = prefix_sums_double[j] - base
  result += passed_count * L

print(result)