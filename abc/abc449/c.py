from collections import defaultdict
import bisect

N, L, R = map(int, input().split())
S = input()

char_positions = defaultdict(list)

for i, c in enumerate(S):
  char_positions[c].append(i)

answer = 0

for char, positions in char_positions.items():
  for i in range(len(positions)):
    left = bisect.bisect_left(positions, positions[i] + L, i + 1)
    right = bisect.bisect_right(positions, positions[i] + R, i + 1)
    answer += right - left

print(answer)