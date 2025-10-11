N = int(input())

def f(n):
  sum = 0
  while n > 0:
    sum += n % 10
    n //= 10
  return sum

As = []
As.append(1)

for i in range(N):
  sum = 0
  for j in range(i + 1):
    sum += f(As[j])
  As.append(sum)

print(As[-1])