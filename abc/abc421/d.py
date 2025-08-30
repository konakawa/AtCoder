Rt, Ct, Ra, Ca = map(int, input().split())
N, M, L = map(int, input().split())

cur = 0
t_moves = []
for _ in range(M):
  S, A = input().split()
  A = int(A)
  t_moves.append(('T', S, cur, A))
  cur += A

cur = 0
a_moves = []
for _ in range(L):
  T, B = input().split()
  B = int(B)
  a_moves.append(('A', T, cur, B))
  cur += B

t_move = t_moves[0]
a_move = a_moves[0]

both_moves = []
t_idx = 1
a_idx = 1

while t_idx < len(t_moves) and a_idx < len(a_moves):
  if t_moves[t_idx][2] <= a_moves[a_idx][2]:
    both_moves.append(t_moves[t_idx])
    t_idx += 1
  else:
    both_moves.append(a_moves[a_idx])
    a_idx += 1

while t_idx < len(t_moves):
  both_moves.append(t_moves[t_idx])
  t_idx += 1

while a_idx < len(a_moves):
  both_moves.append(a_moves[a_idx])
  a_idx += 1

if both_moves:
  last_move = both_moves[-1]
else:
  last_move = t_move
both_moves.append((last_move[0], last_move[1], N, 0))

def format_move(dir, length):
  if dir == 'U':
    return (-length, 0)
  elif dir == 'D':
    return (length, 0)
  elif dir == 'L':
    return (0, -length)
  elif dir == 'R':
    return (0, length)

def cross_check(t_dir, a_dir, length, Rt, Ct, Ra, Ca):
  diff_x = Ra - Rt
  diff_y = Ca - Ct

  move_x = 0
  move_y = 0

  dx, dy = format_move(t_dir, length)

  move_x += dx
  move_y += dy

  dx, dy = format_move(a_dir, length)

  move_x -= dx
  move_y -= dy

  if diff_x != 0 and diff_y != 0:
    return (abs(diff_x) == abs(diff_y)) and (move_x * diff_x) > 0 and (abs(move_x) >= abs(diff_x)) and (move_y * diff_y) > 0 and (abs(move_y) >= abs(diff_y))
  elif diff_x == 0 and diff_y != 0:
    return (diff_y % 2 == 0) and (move_y * diff_y) > 0 and (abs(move_y) >= abs(diff_y)) and (move_x == 0)
  elif diff_y == 0 and diff_x != 0:
    return (diff_x % 2 == 0) and (move_x * diff_x) > 0 and (abs(move_x) >= abs(diff_x)) and (move_y == 0)
  else:
    return False

count = 0
cur = 0
for next_move in both_moves:
  length = next_move[2] - cur

  t_dir = t_move[1]
  a_dir = a_move[1]
  
  if Rt == Ra and Ct == Ca and t_dir == a_dir:
    count += length
  elif cross_check(t_dir, a_dir, length, Rt, Ct, Ra, Ca):
    count += 1
  
  diff_t_x, diff_t_y = format_move(t_dir, length)
  diff_a_x, diff_a_y = format_move(a_dir, length)

  Rt += diff_t_x
  Ct += diff_t_y
  Ra += diff_a_x
  Ca += diff_a_y

  if next_move[0] == 'T':
    t_move = next_move
  else:
    a_move = next_move

  cur = next_move[2]

print(count)