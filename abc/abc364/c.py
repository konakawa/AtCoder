n, x, y = map(int, input().split())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

sorted_As = sorted(As, reverse=True)
sorted_Bs = sorted(Bs, reverse=True)

sweet = 0
sweet_count = 0
while sweet <= x and sweet_count < n:
    sweet += sorted_As[sweet_count]
    sweet_count += 1

salty = 0
salty_count = 0
while salty <= y and salty_count < n:
    salty += sorted_Bs[salty_count]
    salty_count += 1

print(min(sweet_count, salty_count))