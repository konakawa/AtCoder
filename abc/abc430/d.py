N = int(input())
Xs = list(map(int, input().split()))

from sortedcontainers import SortedList

sl = SortedList()
sl.add(0)

result = 0

def nearest_dist(sl, i):
  n = len(sl)
  if n == 1:
    return 0
  d = float('inf')
  if i > 0:
    d = min(d, sl[i] - sl[i - 1])
  if i < n - 1:
    d = min(d, sl[i + 1] - sl[i])
  return d

for x in Xs:
  i = sl.bisect_left(x)

  current_left_dist = 0
  current_right_dist = 0
  if i > 0:
    current_left_dist = nearest_dist(sl, i - 1)
  if i < len(sl):
    current_right_dist = nearest_dist(sl, i)

  sl.add(x)

  x_dist = nearest_dist(sl, i)
  result += x_dist

  if i > 0:
    next_left_dist = nearest_dist(sl, i - 1)
    result += next_left_dist - current_left_dist
  if i < len(sl) - 1:
    next_right_dist = nearest_dist(sl, i + 1)
    result += next_right_dist - current_right_dist

  print(result)