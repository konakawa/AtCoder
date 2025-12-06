N = int(input())
As = list(map(int, input().split()))

count = 0
for l in range(N):
  for r in range(l, N):
    sumA = sum(As[l:r + 1])
    is_valid = True
    for i in range(l, r + 1):
      if sumA % As[i] == 0:
        is_valid = False
        break
    if is_valid:
      count += 1

print(count)