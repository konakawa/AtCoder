def min_ops_to_make(S, target):
  n = len(S)
  bad = '1' if target == '0' else '0'

  next_bad = [n] * (n + 1)
  last = n
  for i in range(n - 1, -1, -1):
    if S[i] == bad:
      last = i
    next_bad[i] = last

  prev_bad = [-1] * (n + 1)
  last = -1
  for i in range(n):
    if S[i] == bad:
      last = i
    prev_bad[i] = last
  prev_bad[n] = prev_bad[n - 1] if n > 0 else -1

  l, r = 0, n - 1
  cost = 0
  while True:
    if next_bad[l] > r:
      break

    if S[l] != bad and S[r] != bad:
      dl = next_bad[l] - l
      dr = r - prev_bad[r]
      if dl <= dr:
        l += 1
      else:
        r -= 1
      cost += 2
    else:
      if S[l] == bad:
        l += 1
        cost += 1
      if l <= r and S[r] == bad:
        r -= 1
        cost += 1
  return cost

def solve(S):
  return min(min_ops_to_make(S, '0'), min_ops_to_make(S, '1'))

T = int(input())

for _ in range(T):
  N = int(input())
  S = input().strip()
  
  print(solve(S))
