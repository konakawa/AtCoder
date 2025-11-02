N = int(input())
As = list(map(int, input().split()))

prefix_max_from_left = [0]
for i in range(N):
  prefix_max_from_left.append(max(prefix_max_from_left[-1], As[i]))

prefix_max_from_right = [0]
for i in range(N - 1, -1, -1):
  prefix_max_from_right.append(max(prefix_max_from_right[-1], As[i]))

prefix_max_from_right.reverse()

D = int(input())

results = []
for i in range(D):
  L, R = map(int, input().split())
  L -= 1
  R -= 1
  result = max(prefix_max_from_left[L], prefix_max_from_right[R + 1])
  results.append(result)

for result in results:
  print(result)