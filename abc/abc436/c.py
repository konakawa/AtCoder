N, M = map(int, input().split())

blocked = set()
count = 0

for _ in range(M):
  R, C = map(int, input().split())
  
  cells = [(R, C), (R, C + 1), (R + 1, C), (R + 1, C + 1)]

  can_place = all(cell not in blocked for cell in cells)
  if can_place:
    count += 1
    for cell in cells:
      blocked.add(cell)

print(count)