X, Y = map(int, input().split())

def f(n):
  result = 0
  while n > 0:
    result *= 10
    result += n % 10
    n //= 10
  return result

As = []
As.append(X)
As.append(Y)

for i in range(2, 10):
  As.append(f(As[i - 1] + As[i - 2]))

print(As[9])