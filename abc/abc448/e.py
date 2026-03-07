K, M = map(int, input().split())

MOD = 10007 * M

def compose(f, g):
  a1, b1 = f
  a2, b2 = g
  return (a1 * a2 % MOD, (b1 * a2 + b2) % MOD)

def repeat_transform(digit, length):
  base = (10, digit)

  result = (1, 0)

  while length > 0:
    if length & 1:
      result = compose(result, base)
    base = compose(base, base)
    length >>= 1

  return result

current = 0

for _ in range(K):
  c, l = map(int, input().split())
  
  a, b = repeat_transform(c, l)
  current = (current * a + b) % MOD

print(current // M)