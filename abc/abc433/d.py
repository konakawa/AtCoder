N, M = map(int, input().split())
As = list(map(int, input().split()))

from collections import Counter, defaultdict
mod_occurrences = Counter(a % M for a in As)

from math import gcd

by_len = defaultdict(list)
for A in As:
  by_len[len(str(A))].append(A)

ans = 0

for digit_count, As_sub in by_len.items():
  coeff = pow(10, digit_count, M)

  lhss = Counter()
  for r, count in mod_occurrences.items():
    y = (r * coeff) % M
    lhss[y] += count

  for A in As_sub:
    rhs = (- A) % M
    ans += lhss.get(rhs, 0)

print(ans)