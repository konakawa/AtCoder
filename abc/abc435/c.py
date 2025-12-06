N = int(input())
As = list(map(int, input().split()))

reach = As[0]
count = 0

for i in range(N):
  if i >= reach:
    break

  reach = max(reach, i + As[i])
  count += 1

print(count)