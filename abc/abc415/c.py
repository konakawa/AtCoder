T = int(input())

for _ in range(T):
  N = int(input())
  S = input()

  routes = set()
  routes.add(0)

  for i, s in enumerate(S):
    if s == '0':
      can_merge = False

      # iの各桁の1を0にした値がroutesに含まれているかチェックする
      # tempには未確認の桁が1になった値が入っている
      cond = i + 1
      temp = i + 1
      while temp > 0:
        temp_lowest_bit = temp & -temp
        modified = cond ^ temp_lowest_bit
        if modified in routes:
          can_merge = True
          break
        temp ^= temp_lowest_bit
      
      if can_merge:
        routes.add(cond)

  all_bits_set = (1 << N) - 1
  if all_bits_set in routes:
    print("Yes")
  else:
    print("No")
