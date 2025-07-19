N = int(input())
As = list(map(int, input().split()))
X = int(input())

for i, A in enumerate(As):
  if A == X:
    print('Yes')
    exit()

print('No')