MOD = 998244353

N, D = map(int, input().split())
As = list(map(int, input().split()))

As.sort()

factorial = [1] * (N + 1)
for i in range(1, N + 1):
  factorial[i] = factorial[i - 1] * i % MOD

inverse_factorial = [1] * (N + 1)
inverse_factorial[N] = pow(factorial[N], MOD - 2, MOD)
for i in range(N, 0, -1):
  inverse_factorial[i - 1] = inverse_factorial[i] * i % MOD

ans = 1
j = 0
for i in range(N):
  x = As[i] - D
  while j < i and As[j] < x:
    j += 1
  
  ways = i + 1 - j
  ans = (ans * ways) % MOD

from collections import Counter
for count in Counter(As).values():
  ans = (ans * inverse_factorial[count]) % MOD

print(ans % MOD)