N = int(input())

result = 0
for i in range(1, N+1):
  result += (-1) ** i * i ** 3

print(result)