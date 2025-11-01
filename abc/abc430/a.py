A, B, C, D = map(int, input().split())

if A <= C:
  if B > D:
    print('Yes')
    exit()

print('No')