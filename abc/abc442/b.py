Q = int(input())

volume = 0
is_played = False

for _ in range(Q):
  A = int(input())
  if A == 1:
    volume += 1
  elif A == 2:
    volume = max(volume - 1, 0)
  elif A == 3:
    is_played = not is_played

  if is_played and volume >= 3:
    print('Yes')
  else:
    print('No')