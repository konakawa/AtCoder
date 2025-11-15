N, X, Y = map(int, input().split())
storms = []
for _ in range(N):
  C, A, B = input().split()
  A = int(A)
  B = int(B)
  storms.append((C, A, B))

rectangles = [(0, X - 1, 0, Y - 1)]

for C, A, B in storms:
  new_rectangles = []

  if C == 'X':
    for x1, x2, y1, y2 in rectangles:
      if x2 < A:
        new_rectangles.append((x1, x2, y1 - B, y2 - B))
      elif x1 >= A:
        new_rectangles.append((x1, x2, y1 + B, y2 + B))
      else:
        new_rectangles.append((x1, A - 1, y1 - B, y2 - B))
        new_rectangles.append((A, x2, y1 + B, y2 + B))
  else:
    for x1, x2, y1, y2 in rectangles:
      if y2 < A:
        new_rectangles.append((x1 - B, x2 - B, y1, y2))
      elif y1 >= A:
        new_rectangles.append((x1 + B, x2 + B, y1, y2))
      else:
        new_rectangles.append((x1 - B, x2 - B, y1, A - 1))
        new_rectangles.append((x1 + B, x2 + B, A, y2))
  rectangles = new_rectangles

num_rectangles = len(rectangles)
parent = list(range(num_rectangles))
size = [1] * num_rectangles

def find(x):
  while parent[x] != x:
    parent[x] = parent[parent[x]]
    x = parent[x]
  return x

def union(x, y):
  root_x = find(x)
  root_y = find(y)
  if root_x == root_y:
    return

  if size[root_x] < size[root_y]:
    root_x, root_y = root_y, root_x

  parent[root_y] = root_x
  size[root_x] += size[root_y]

indexed = list(enumerate(rectangles))
indexed.sort(key=lambda x: x[1][0])

for i in range(num_rectangles):
  idx_i, rect_i = indexed[i]
  x1_i, x2_i, y1_i, y2_i = rect_i

  for j in range(i + 1, num_rectangles):
    idx_j, rect_j = indexed[j]
    x1_j, x2_j, y1_j, y2_j = rect_j

    if x1_j > x2_i + 1:
      break

    # 重なる
    if max(x1_i, x1_j) <= min(x2_i, x2_j) and max(y1_i, y1_j) <= min(y2_i, y2_j):
      union(idx_i, idx_j)
      continue

    # 上下隣接
    if max(x1_i, x1_j) <= min(x2_i, x2_j) and (y1_j == y2_i + 1 or y1_i == y2_j + 1):
      union(idx_i, idx_j)
      continue

    # 左右隣接
    if max(y1_i, y1_j) <= min(y2_i, y2_j) and (x1_j == x2_i + 1 or x1_i == x2_j + 1):
      union(idx_i, idx_j)
      continue

rectangle_size = {}
for i, (x1, x2, y1, y2) in enumerate(rectangles):
  root = find(i)
  num_cells = (x2 - x1 + 1) * (y2 - y1 + 1)
  rectangle_size[root] = rectangle_size.get(root, 0) + num_cells

sorted_rectangle_size = sorted(rectangle_size.values())

print(len(sorted_rectangle_size))
print(*sorted_rectangle_size)