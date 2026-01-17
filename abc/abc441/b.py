N, M = map(int, input().split())
S = input()
T = input()
Q = int(input())

for _ in range(Q):
  w = input()
  is_in_S = True
  is_in_T = True
  for c in w:
    if c not in S:
      is_in_S = False
    if c not in T:
      is_in_T = False
  if is_in_S and is_in_T:
    print('Unknown')
  elif is_in_S:
    print('Takahashi')
  elif is_in_T:
    print('Aoki')
  else:
    print('Unknown')