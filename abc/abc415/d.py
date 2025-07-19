n, m = map(int, input().split())

menus = []
for _ in range(m):
  a, b = map(int, input().split())
  menus.append((a, b))

count = 0

menus.sort(key=lambda x: x[1] - x[0], reverse=True)

for menu in menus:
  a, b = menu
  if n >= a:
    diff = a - b
    times = (n - a) // diff + 1
    count += times
    n -= times * diff
    if n < 0:
      break

print(count)