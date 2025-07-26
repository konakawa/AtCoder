N, K, X = map(int, input().split())

Ss = []
for _ in range(N):
  Ss.append(input())

patterns = []

def generate_sorted_concat_patterns(current, depth):
  if depth == K:
    patterns.append(current)
    return
  
  for s in Ss:
    generate_sorted_concat_patterns(current + s, depth + 1)

generate_sorted_concat_patterns("", 0)

patterns.sort()

print(patterns[X - 1])
