X, Y, Z = map(int, input().split())

# X + n = (Y + n) * Z
# n = (X - Y * Z) / (Z - 1)

numerator = X - Y * Z
denominator = Z - 1

if numerator % denominator == 0 and numerator >= 0:
  print('Yes')
else:
  print('No')