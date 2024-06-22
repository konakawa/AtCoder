n = int(input())
As = list(map(int, input().split()))

count = 0

for i in range(2*n - 2):
    a_l = As[i]
    a_r = As[i+2]
    if a_l == a_r:
        count += 1

print(count)