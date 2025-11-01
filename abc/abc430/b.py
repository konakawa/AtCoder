N, M = map(int, input().split())

grid = []
for _ in range(N):
  grid.append(list(input()))

patterns = set()

def pattern_to_bitstring(pattern):
  bitstring = ''
  for i in range(M):
    for j in range(M):
      if pattern[i][j] == '#':
        bitstring += '1'
      else:
        bitstring += '0'
  return bitstring

for i in range(N - M + 1):
  for j in range(N - M + 1):
    pattern = []
    for k in range(M):
      pattern.append(grid[i + k][j:j + M])
    patterns.add(pattern_to_bitstring(pattern))

print(len(patterns))