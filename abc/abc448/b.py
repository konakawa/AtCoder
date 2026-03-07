N, M = map(int, input().split())
Cs = list(map(int, input().split()))

result = 0
for i in range(N):
  A, B = map(int, input().split())
  amount_pepper = min(B, Cs[A - 1])
  result += amount_pepper
  Cs[A - 1] -= amount_pepper

print(result)