N, X = map(int, input().split())
As = list(map(int, input().split()))

for i in range(N):
  if As[i] == X:
    print('Yes')
    exit()

print('No')