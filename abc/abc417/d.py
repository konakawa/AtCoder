N = int(input())
presents = []
B_sum = 0
for _ in range(N):
  P, A, B = map(int, input().split())
  presents.append((P, A, B))
  B_sum += B

Q = int(input())

results = []
for _ in range(Q):
  X = int(input())

  # ここと B_sum の定義を入れただけで TLE から AC になってしまったがそれはテストが悪いのでは…？
  if X > B_sum + 501:
    results.append(X - B_sum)
    continue

  for present in presents:
    P, A, B = present
    if X <= P:
      X += A
    else:
      X = max(0, X - B)

  results.append(X)

for result in results:
  print(result)