N = int(input())
Ls = list(map(int, input().split()))

count = 0

for i in range(N):
  if Ls[i] == 0:
    count += 1
  else:
    break

for i in range(N-1, -1, -1):
  if Ls[i] == 0:
    count += 1
  else:
    break

result = (N + 1) - count - 2

if result < 0:
  result = 0

print(result)