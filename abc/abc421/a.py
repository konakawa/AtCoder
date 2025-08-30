N = int(input())
Ss = []
for _ in range(N):
  Ss.append(input())

X, Y = input().split()
X = int(X)

if Ss[X - 1] == Y:
  print('Yes')
else:
  print('No')