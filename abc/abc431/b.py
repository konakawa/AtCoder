X = int(input())
N = int(input())
Ws = list(map(int, input().split()))
Q = int(input())

weight = X
joined = [False] * N

results = []

for _ in range(Q):
  P = int(input())
  if joined[P - 1]:
    weight -= Ws[P - 1]
    joined[P - 1] = False
  else:
    weight += Ws[P - 1]
    joined[P - 1] = True

  results.append(weight)

for result in results:
  print(result)