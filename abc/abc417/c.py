N = int(input())
As = list(map(int, input().split()))

from collections import Counter

added_As = Counter()
for i in range(N):
  added_As[As[i] + i + 1] += 1

count = 0

for j in range(N):
  target = (j + 1) - As[j]
  count += added_As[target]

print(count)
