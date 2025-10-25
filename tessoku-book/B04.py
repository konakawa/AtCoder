N = input()

result = 0
for i in range(len(N)):
  result += int(N[i]) * (2 ** (len(N) - i - 1))

print(result)