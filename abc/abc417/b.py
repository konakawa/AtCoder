N, M = map(int, input().split())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

for B in Bs:
  if B in As:
    As.remove(B)

if len(As) > 0:
  print(" ".join(map(str, As)))