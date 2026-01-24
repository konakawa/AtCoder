import cmath
import bisect
from math import gcd
from collections import Counter
from functools import cmp_to_key

N, Q = map(int, input().split())
monsters = []
for _ in range(N):
  X, Y = map(int, input().split())
  monsters.append((X, Y))

def normalize(x, y):
  g = gcd(abs(x), abs(y))
  return (x // g, y // g)

def get_half(direction):
  x, y = direction
  if y > 0 or (y == 0 and x > 0):
    return 0
  else:
    return 1

def compare(dir1, dir2):
  h1, h2 = get_half(dir1), get_half(dir2)

  if h1 != h2:
    return h1 - h2

  cross = dir1[0] * dir2[1] - dir1[1] * dir2[0]
  if cross > 0:
    return -1
  elif cross < 0:
    return 1
  else:
    return 0

directions  = [normalize(x, y) for x, y in monsters]
dir_count   = Counter(directions)
unique_dirs = list(dir_count.keys())
sorted_dirs = sorted(unique_dirs, key=cmp_to_key(compare))
dir_to_idx  = {dir: i for i, dir in enumerate(sorted_dirs)}

M = len(sorted_dirs)
prefix_sums = [0] * (M + 1)
for i in range(M):
  prefix_sums[i + 1] = prefix_sums[i] + dir_count[sorted_dirs[i]]

monster_dir_idx = [dir_to_idx[directions[i]] for i in range(N)]

for _ in range(Q):
  A, B = map(int, input().split())
  idx_start = monster_dir_idx[A - 1]
  idx_end = monster_dir_idx[B - 1]

  if idx_start >= idx_end:
    count = prefix_sums[idx_start + 1] - prefix_sums[idx_end]
  else:
    count = (prefix_sums[M] - prefix_sums[idx_end]) + prefix_sums[idx_start + 1]
  
  print(count)