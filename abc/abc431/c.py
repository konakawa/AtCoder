N, M, K = map(int, input().split())
Hs = list(map(int, input().split()))
Bs = list(map(int, input().split()))

sorted_Hs = sorted(Hs)
sorted_Bs = sorted(Bs)

i = 0
j = 0

count = 0

while i < N and j < M:
  if sorted_Hs[i] <= sorted_Bs[j]:
    i += 1
    j += 1
    count += 1
  else:
    j += 1

if count >= K:
  print("Yes")
else:
  print("No")