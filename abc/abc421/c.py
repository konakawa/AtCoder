N = int(input())
S = input()

A_positions = []
for i, s in enumerate(S):
  if s == 'A':
    A_positions.append(i)

count_AB = 0

for i in range(N):
  diff = abs(A_positions[i] - (2 * i))
  count_AB += diff

count_BA = 0

for i in range(N):
  diff = abs(A_positions[i] - (2 * i + 1))
  count_BA += diff

print(min(count_AB, count_BA))