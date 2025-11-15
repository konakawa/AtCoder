A, B, C = map(int, input().split())
l = [A, B, C]
l.sort()
print(l[0] + l[1] * 10 + l[2] * 100)