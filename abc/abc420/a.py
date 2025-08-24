X, Y = map(int, input().split())

result = (X + Y) % 12

if result == 0:
  print(12)
else:
  print(result)