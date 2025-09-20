def grid_to_bits(grid):
  bits = []
  for i in range(len(grid)):
    bit = 0
    for j in range(len(grid[i])):
      if grid[i][j] == '#':
        bit |= 1 << j
    bits.append(bit)
  return bits

def bits_to_subsets(bits):
  subsets = []
  s = bits
  while s > 0:
    subsets.append(s)
    s = (s - 1) & bits
  subsets.append(0)
  return subsets

def solve():
  H, W = map(int, input().split())
  grid = []
  for _ in range(H):
    grid.append(list(input()))

  bits = grid_to_bits(grid)
  
  total_black = sum(bit.bit_count() for bit in bits)
  
  subs_s = [bits_to_subsets(bit) for bit in bits]

  dp_prev = {m: m.bit_count() for m in subs_s[0]}

  for i in range(1, H):
    dp_current = {}
    for cur, cur_count in dp_prev.items():
      for next_candidate in subs_s[i]:
        if (cur & (cur << 1) & next_candidate & (next_candidate << 1)) == 0:
          next_count = cur_count + next_candidate.bit_count()
          if next_count > dp_current.get(next_candidate, float('-inf')):
            dp_current[next_candidate] = next_count
    dp_prev = dp_current

  max_black = max(dp_prev.values())
  print(total_black - max_black)

T = int(input())

for _ in range(T):
  solve()