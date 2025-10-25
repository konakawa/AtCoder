N, M = map(int, input().split())
As = list(map(int, input().split()))

sum = 0
for i in range(N):
  sum += As[i]

for i in range(N):
  if sum - As[i] == M:
    print('Yes')
    exit()

print('No')