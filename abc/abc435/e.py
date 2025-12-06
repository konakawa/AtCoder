from sortedcontainers import SortedList

N, Q = map(int, input().split())

intervals = SortedList()
black_len = 0

for _ in range(Q):
  L, R = map(int, input().split())
  newL, newR = L, R

  to_remove = []

  pos = intervals.bisect_left((L, -1))
  if pos > 0:
    s, e = intervals[pos - 1]
    if e >= L - 1:
      newL = min(newL, s)
      newR = max(newR, e)
      to_remove.append((s, e))

  while pos < len(intervals):
    s, e = intervals[pos]
    if s > newR + 1:
      break
    newL = min(newL, s)
    newR = max(newR, e)
    to_remove.append((s, e))
    pos += 1

  for interval in to_remove:
    black_len -= interval[1] - interval[0] + 1
    intervals.remove(interval)

  black_len += newR - newL + 1
  intervals.add((newL, newR))

  print(N - black_len)