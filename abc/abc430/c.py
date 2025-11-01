N, A, B = map(int, input().split())
S = input()

r_lefts = [-1] * N
r_rights = [-1] * N

r = 0
a_count = 0
for l in range(N):
  while r < N and a_count < A:
    if S[r] == 'a':
      a_count += 1
    r += 1

  if a_count >= A:
    r_lefts[l] = r - 1
  else:
    r_lefts[l] = -1
  
  if S[l] == 'a':
    a_count -= 1


r = 0
b_count = 0
for l in range(N):
  while r < N and b_count + (1 if S[r] == 'b' else 0) < B:
    if S[r] == 'b':
      b_count += 1
    r += 1

  r_rights[l] = r - 1

  if S[l] == 'b':
    b_count -= 1

result = 0
for i in range(N):
  L = r_lefts[i]
  R = r_rights[i]
  if L != -1 and L <= R:
    result += R - L + 1

print(result)