N, R = map(int, input().split())
Ls = list(map(int, input().split()))

L_index = -1
R_index = -1

for i in range(R):
  if Ls[i] == 0:
    L_index = i
    break

for i in range(N-1, R-1, -1):
  if Ls[i] == 0:
    R_index = i + 1
    break

if L_index == -1:
  L_index = R
if R_index == -1:
  R_index = R

count = 0
for i in range(L_index, R_index):
  count += 1 + Ls[i]

print(count)