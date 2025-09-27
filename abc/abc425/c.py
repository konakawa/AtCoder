N, Q = map(int, input().split())
As = list(map(int, input().split()))

sums = [0] * (N + 1)
for i in range(N):
  sums[i + 1] = sums[i] + As[i]

offset = 0

results = []

for _ in range(Q):
  query = input().split()

  if query[0] == '1':
    c = int(query[1]) % N
    offset = (offset + c) % N
  else:
    l = int(query[1])
    r = int(query[2])
    L = (offset + l - 1) % N
    R = (offset + r - 1) % N
    if L <= R:
      results.append(sums[R + 1] - sums[L])
    else:
      results.append((sums[N] - sums[L]) + sums[R + 1])

for result in results:
  print(result)