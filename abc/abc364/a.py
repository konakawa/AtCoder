n = int(input())
prev = 'salty'
f = False
f2 = False

for i in range(n):
    s = input()
    if f:
        f2 = True
    if prev == 'sweet' and s == 'sweet':
        f = True
    prev = s

if f2:
    print('No')
else:
    print('Yes')