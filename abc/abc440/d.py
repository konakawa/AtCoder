from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
As = list(map(int, input().split()))
As.sort()

for _ in range(Q):
  X, Y = map(int, input().split())
  
  start = bisect_left(As, X)
  lo, hi = start, N
  while lo < hi:
    mid = (lo + hi) // 2
    gaps = As[mid] - X - (mid - start)
    if gaps < Y:
      lo = mid + 1
    else:
      hi = mid

  skip = lo - start
  
  print(X + Y - 1 + skip)