N = int(input())
As = list(map(int, input().split()))

from collections import defaultdict
num_occurrences = defaultdict(int)

for i in range(N):
  num_occurrences[As[i]] += 1

result = 0

if len(num_occurrences) <= 1:
  print(result)
  exit()

for i in range(1, N + 1):
  occurrence = num_occurrences[i]
  if occurrence > 1:
    result += (occurrence * (occurrence - 1) // 2) * (N - occurrence)

print(result)