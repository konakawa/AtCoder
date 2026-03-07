N, Q = map(int, input().split())
As = list(map(int, input().split()))

indexed_As = [(i + 1, A) for i, A in enumerate(As)]
sorted_indexed_As = sorted(indexed_As, key=lambda x: x[1])

A1_index = sorted_indexed_As[0][0]
A2_index = sorted_indexed_As[1][0]
A3_index = sorted_indexed_As[2][0]
A4_index = sorted_indexed_As[3][0]
A5_index = sorted_indexed_As[4][0]

for i in range(Q):
  K = int(input())
  Bs = set(map(int, input().split()))

  ans = sorted_indexed_As[K][1]

  if not A1_index in Bs:
    ans = sorted_indexed_As[0][1]
  elif not A2_index in Bs:
    ans = sorted_indexed_As[1][1]
  elif not A3_index in Bs:
    ans = sorted_indexed_As[2][1]
  elif not A4_index in Bs:
    ans = sorted_indexed_As[3][1]
  elif not A5_index in Bs:
    ans = sorted_indexed_As[4][1]

  print(ans)