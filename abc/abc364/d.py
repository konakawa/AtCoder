n, q = map(int, input().split())
As = list(map(int, input().split()))
sorted_As = sorted(As)

import bisect
def find_kth_nearest_point(sorted_As, x, k):
    idx = bisect.bisect_left(sorted_As, x)
    
    left = idx - 1
    right = idx
    if k == 1:
        return sorted_As[left] if abs(sorted_As[left] - x) <= abs(sorted_As[right] - x) else sorted_As[right]
    count = 0
    if left >= 0:
        count += 1
    if right < len(sorted_As):
        count += 1

    while count < k:
        if left >= 0 and (right >= len(sorted_As) or abs(sorted_As[left] - x) <= abs(sorted_As[right] - x)):
            left -= 1
            if left < 0:
                right += 1
        else:
            right += 1
            if right >= len(sorted_As):
                left -= 1
        count += 1

    if left < 0:
        return sorted_As[right]
    elif right >= len(sorted_As):
        return sorted_As[left]
    else:
        return sorted_As[left] if abs(sorted_As[left] - x) >= abs(sorted_As[right] - x) else sorted_As[right]

result_list = []
for _ in range(q):
    b, k = map(int, input().split())
    d = abs(find_kth_nearest_point(sorted_As, b, k) - b)
    result_list.append(d)

for result in result_list:
    print(result)