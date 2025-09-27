N = int(input())
As = list(map(int, input().split()))

num_occurrences = {}
for i in range(N):
  num_occurrences[i + 1] = 0

for A in As:
  if A == -1:
    continue
  if A in num_occurrences:
    num_occurrences[A] += 1

has_duplicate = any(count >= 2 for count in num_occurrences.values())
if has_duplicate:
  print("No")
else:
  print("Yes")

  Ps = []
  for A in As:
    if A != -1:
      Ps.append(A)
    else:
      for i in range(1, N+1):
        if num_occurrences[i] == 0:
          Ps.append(i)
          num_occurrences[i] = 1
          break

  print(" ".join(map(str, Ps)))