N = int(input())
Ps = list(map(int, input().split()))

visited = [False] * N
ans = 0

for i in range(N):
  if visited[i]:
    continue

  cycle_len = 0
  j = i
  while not visited[j]:
    visited[j] = True
    j = Ps[j] - 1
    cycle_len += 1

  ans += cycle_len * (cycle_len - 1) // 2

print(ans)