S = input()

prev_num     = -1
current_num  = int(S[0])
count_first  = 0
count_second = 0

count_result = 0

for i in range(len(S)):
  n = int(S[i])
  if current_num != n:
    if prev_num + 1 == current_num:
      count_result += min(count_first, count_second)

    prev_num     = current_num
    current_num  = n
    count_first  = count_second
    count_second = 1
  else:
    count_second += 1

if prev_num + 1 == current_num:
  count_result += min(count_first, count_second)

print(count_result)