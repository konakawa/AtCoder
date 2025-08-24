N, L = map(int, input().split())
K = int(input())
As = list(map(int, input().split()))

def can_cut_above(n):
  remain_k = K
  current = 0
  for i in range(N):
    if remain_k == 0:
      return L - current >= n
    
    if As[i] - current >= n:
      remain_k -= 1
      current = As[i]

  return remain_k == 0 and L - current >= n

left = -1
right = L + 1
while right - left > 1:
  mid = (left + right) // 2
  if can_cut_above(mid):
    left = mid
  else:
    right = mid

print(left)