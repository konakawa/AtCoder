X, Y = input().split()

result = False

if X == 'Lynx':
  result = True
elif X == 'Serval':
  if Y == 'Ocelot' or Y == 'Serval':
    result = True
elif X == 'Ocelot':
  if Y == 'Ocelot':
    result = True

if result:
  print('Yes')
else:
  print('No')