N = int(input())

def is_ok(n):
  count_open_paren = 0
  for i in range(N - 1, -1, -1):
    if (n >> i) & 1:
      count_open_paren -= 1
    else:
      count_open_paren += 1
    if count_open_paren < 0:
      return False
  return count_open_paren == 0

def str_paren(n):
  s = ""
  for i in range(N - 1, -1, -1):
    if (n >> i) & 1:
      s += ")"
    else:
      s += "("
  return s

for bit in range(1 << N):
  if is_ok(bit):
    print(str_paren(bit))