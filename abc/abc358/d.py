n, m = map(int, input().split())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

As.sort()
Bs.sort()

sum = 0

i = 0
j = 0

while i < n and j < m:
    if As[i] >= Bs[j]:
        sum += As[i]
        i += 1
        j += 1
    elif As[i] < Bs[j]:
        i += 1

if j == m:
    print(sum)
else:
    print(-1)