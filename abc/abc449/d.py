def count_in_first_quadrant_excluding_axis(R, U):
  white = 0
  black = 0

  lo = min(R, U)
  hi = max(R, U)
  
  adding_white = 1
  points = 1
  for i in range(1, lo + 1):
    if adding_white:
      white += points
    else:
      black += points
    adding_white = not adding_white
    points += 2

  for i in range(lo + 1, hi + 1):
    if adding_white:
      white += lo
    else:
      black += lo
    adding_white = not adding_white

  return white, black

def calc_rect_first_quadrant(L, R, D, U):
  def count(R, U):
    if R <= 0 or U <= 0:
      return (0, 0)
    return count_in_first_quadrant_excluding_axis(R, U)

  def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])
  def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

  result = count(R, U)
  result = sub(result, count(L - 1, U))
  result = sub(result, count(R, D - 1))
  result = add(result, count(L - 1, D - 1))
  return result

def count_on_axis(L, R, D, U):
  white = 0
  black = 0

  if D <= 0 <= U:
    total = R - L + 1
    evens = R // 2 - (L - 1) // 2
    black += evens
    white += total - evens
  
  if L <= 0 <= R:
    total = U - D + 1
    evens = U // 2 - (D - 1) // 2
    black += evens
    white += total - evens
  
  if L <= 0 <= R and D <= 0 <= U:
    black -= 1

  return white, black

L, R, D, U = map(int, input().split())

total_white = 0
total_black = 0

if R >= 1 and U >= 1:
  white, black = calc_rect_first_quadrant(max(L, 1), R, max(D, 1), U)
  total_white += white
  total_black += black

if L <= -1 and U >= 1:
  white, black = calc_rect_first_quadrant(max(-R, 1), -L, max(D, 1), U)
  total_white += white
  total_black += black

if L <= -1 and D <= -1:
  white, black = calc_rect_first_quadrant(max(-R, 1), -L, max(-U, 1), -D)
  total_white += white
  total_black += black

if D <= -1 and R >= 1:
  white, black = calc_rect_first_quadrant(max(L, 1), R, max(-U, 1), -D)
  total_white += white
  total_black += black

white, black = count_on_axis(L, R, D, U)
total_white += white
total_black += black

print(total_black)