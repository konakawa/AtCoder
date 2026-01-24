N, Q = map(int, input().split())
As = list(map(int, input().split()))

prefix_sums = [0]
for A in As:
  prefix_sums.append(prefix_sums[-1] + A)

for _ in range(Q):
  query = input().split()
  if query[0] == '1':
    x = int(query[1])
    As[x - 1], As[x] = As[x], As[x - 1]
    prefix_sums[x] = prefix_sums[x - 1] + As[x - 1]
  elif query[0] == '2':
    l, r = int(query[1]), int(query[2])
    print(prefix_sums[r] - prefix_sums[l - 1])
