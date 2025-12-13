N = int(input())
Bs = list(map(int, input().split()))

Ps = [0] * (N + 1)
for i in range(N):
  Ps[Bs[i]] = i

bit = [0] * (N + 1)

def add(i):
  i += 1
  while i <= N:
    bit[i] += 1
    i += i & (-i)

def query(i):
  i += 1
  s = 0
  while i > 0:
    s += bit[i]
    i -= i & (-i)
  return s

ans = 0
for b in range(1, N + 1):
  P = Ps[b]
  add(P)
  L = query(P)
  R = b - query(P - 1)
  ans += L * R

print(ans)