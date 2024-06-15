n, a = map(int, input().split())
ts = list(map(int, input().split()))

prev = 0

for t in ts:
    if prev <= t:
        prev = t + a
    else:
        prev += a
    print(prev)
    