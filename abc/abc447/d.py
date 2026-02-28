S = input()

from collections import deque

A_positions = deque()
B_positions = deque()
C_positions = deque()

for i, c in enumerate(S):
  if c == 'A':
    A_positions.append(i)
  elif c == 'B':
    B_positions.append(i)
  elif c == 'C':
    C_positions.append(i)

count = 0
while A_positions and B_positions and C_positions:
  a_pos = A_positions.popleft()

  b_pos = -1
  while B_positions and b_pos < a_pos:
    b_pos = B_positions.popleft()
  if b_pos < a_pos:
    break

  c_pos = -1
  while C_positions and c_pos < b_pos:
    c_pos = C_positions.popleft()
  if c_pos < b_pos:
    break

  count += 1

print(count)