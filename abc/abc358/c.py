n, m = map(int, input().split())

ss = [input() for _ in range(n)]

def combine(ss):
    result = []
    for i in range(m):
        if any(s[i] == 'o' for s in ss):
            result.append('o')
        else:
            result.append('x')
    return ''.join(result)

from itertools import combinations

for i in range(n+1):
    for cs in combinations(ss, i):
        combined = combine(cs)
        if all(c == 'o' for c in combined):
            print(i)
            exit()