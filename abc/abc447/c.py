S = input()
T = input()

S_except_A = S.replace('A', '')
T_except_A = T.replace('A', '')

if S_except_A != T_except_A:
  print(-1)
  exit()

len_S = len(S)
len_T = len(T)
len_S_except_A = len(S_except_A)


gaps_S = [0] * (len_S_except_A + 1)
gaps_T = [0] * (len_S_except_A + 1)

count = 0
j = 0
for i in range(len_S):
  if S[i] != 'A':
    gaps_S[j] = count
    j += 1
    count = 0
  else:
    count += 1
gaps_S[j] = count


count = 0
j = 0
for i in range(len_T):
  if T[i] != 'A':
    gaps_T[j] = count
    j += 1
    count = 0
  else:
    count += 1
gaps_T[j] = count

result = 0
for gap_S, gap_T in zip(gaps_S, gaps_T):
  result += abs(gap_S - gap_T)

print(result)